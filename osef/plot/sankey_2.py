


from collections import defaultdict
from matplotlib import gridspec

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class PySankeyException(Exception):
    pass


class NullsInFrame(PySankeyException):
    pass


class LabelMismatch(PySankeyException):
    pass

class Sankey:

    def __init__(self):
        self.i_max = 0
        self.i_change = 2


    def plot_sankey(self, values_flows, connect, title='', show=True):
            """
            This method call the Sankey function of matplotlib to plot a Sankey. For the variable connect, the key is the
            start of the flow and the value is the end of the flow

            Example:
            values_flows = {'ini1':1000, 'ini2':3000, 'mid1': 200, 'mid2': 5000, 'out1': 1500, 'out2':1500}
            connect =  [('ini1', 'mid1'),
                        ('ini1', 'mid2'),
                        ('ini2', 'mid2'),
                        ('mid1', 'end1'),
                        ('mid1', 'end2'),
                        ('mid2', 'end2')]

            :param values_flows: a dict with the name and the value of each flows
            :param connect: a  list of tuble (start, end) describing the connection using the same labels as values_flows
            :param title: A string which is the title of the figure
            :param show: If True the figure is shown otherwise not
            """
            figure=plt.figure()
            plt.title(title)
            gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 1],wspace=0.0, hspace=0.0)

            # get the flow which are the start of the graphic(level0)
            start_value = [k[0] for k in connect]
            end_value = [k[1] for k in connect]
            level_ind = [ind for ind, s in enumerate(start_value) if s not in end_value]

            # make one Sankey by level
            ind = 1
            while len(level_ind) > 0 and ind < 200:
                plt.subplot(gs[0, ind-1])

                # get label of the flows at this level
                label_in = sorted([c[0] for ind, c in enumerate(connect) if ind in level_ind])
                label_out = sorted([c[1] for ind, c in enumerate(connect) if ind in level_ind])


                # get flow at this level
                flow_in = [values_flows[la] for la in label_in]
                flow_out = [values_flows[la] for la in label_out]

                # get new level in
                level_ind = [ind for ind, s in enumerate(start_value) if s in label_out]

                # avoid having double label
                # if ind > 1:
                #     label_in = [''] * len(label_in)

                # plot
                self.sankey_one_step(label_in, label_out, leftWeight=flow_in, rightWeight=flow_out)

                ind +=1

            if show:
                plt.show()


    def sankey_one_step(self, left, right, leftWeight=None, rightWeight=None, colorDict=None,
               leftLabels=None, rightLabels=None, aspect=4, rightColor=False,
               fontsize=14):
        """
        Produces simple Sankey Diagrams with matplotlib.
        @author: Anneya Golob & marcomanz & pierre-sassoulas & jorwoods
                              .-.
                         .--.(   ).--.
              <-.  .-.-.(.->          )_  .--.
               `-`(     )-'             `)    )
                 (o  o  )                `)`-'
                (      )                ,)
                ( ()  )                 )
                 `---"\    ,    ,    ,/`
                       `--' `--' `--'
                        |  |   |   |
                        |  |   |   |
                        '  |   '   |

        Make Sankey Diagram showing flow from left-->right for one step
        Inputs:
            figure = matplotlib figure which contain the sankey for all the step
            left = NumPy array of object labels on the left of the diagram
            right = NumPy array of corresponding labels on the right of the diagram
                len(right) == len(left)
            leftWeight = NumPy array of weights for each strip starting from the
                left of the diagram, if not specified 1 is assigned
            rightWeight = NumPy array of weights for each strip starting from the
                right of the diagram, if not specified the corresponding leftWeight
                is assigned
            colorDict = Dictionary of colors to use for each label
                {'label':'color'}
            leftLabels = order of the left labels in the diagram
            rightLabels = order of the right labels in the diagram
            aspect = vertical extent of the diagram in units of horizontal extent
            rightColor = If true, each strip in the diagram will be be colored
                        according to its left label
        Ouput:
            None
        """

        if leftWeight is None:
            leftWeight = []
        if rightWeight is None:
            rightWeight = []
        if leftLabels is None:
            leftLabels = []
        if rightLabels is None:
            rightLabels = []
        # Check weights
        if len(leftWeight) == 0:
            leftWeight = np.ones(len(left))

        if len(rightWeight) == 0:
            rightWeight = leftWeight

        plt.rc('text', usetex=False)
        plt.rc('font', family='serif')

        # Create Dataframe
        if isinstance(left, pd.Series):
            left = left.reset_index(drop=True)
        if isinstance(right, pd.Series):
            right = right.reset_index(drop=True)
        dataFrame = pd.DataFrame({'left': left, 'right': right, 'leftWeight': leftWeight,
                                  'rightWeight': rightWeight}, index=range(len(left)))

        if len(dataFrame[(dataFrame.left.isnull()) | (dataFrame.right.isnull())]):
            raise NullsInFrame('Sankey graph does not support null values.')

        # Identify all labels that appear 'left' or 'right'
        allLabels = pd.Series(np.r_[dataFrame.left.unique(), dataFrame.right.unique()]).unique()

        # Identify left labels
        if len(leftLabels) == 0:
            leftLabels = pd.Series(dataFrame.left.unique()).unique()
        else:
            check_data_matches_labels(leftLabels, dataFrame['left'], 'left')

        # Identify right labels
        if len(rightLabels) == 0:
            rightLabels = pd.Series(dataFrame.right.unique()).unique()
        else:
            check_data_matches_labels(leftLabels, dataFrame['right'], 'right')

        # If no colorDict given, make one
        i=0
        if colorDict is None:
            colorDict = {}
            cm = plt.get_cmap('gist_rainbow')
            for i, label in enumerate(allLabels):
                colorDict[label] = cm((i+self.i_max) / (self.i_max +len(allLabels)))
        else:
            missing = [label for label in allLabels if label not in colorDict.keys()]
            if missing:
                msg = "The colorDict parameter is missing values for the following labels : "
                msg += '{}'.format(', '.join(missing))
                raise ValueError(msg)
        self.i_max +=i + self.i_change

        # Determine widths of individual strips
        ns_l = defaultdict()
        ns_r = defaultdict()
        for leftLabel in leftLabels:
            leftDict = {}
            rightDict = {}
            for rightLabel in rightLabels:
                leftDict[rightLabel] = dataFrame[(dataFrame.left == leftLabel) & (dataFrame.right == rightLabel)].leftWeight.sum()
                rightDict[rightLabel] = dataFrame[(dataFrame.left == leftLabel) & (dataFrame.right == rightLabel)].rightWeight.sum()
            ns_l[leftLabel] = leftDict
            ns_r[leftLabel] = rightDict

        # Determine positions of left label patches and total widths
        leftWidths = defaultdict()
        for i, leftLabel in enumerate(leftLabels):
            myD = {}
            myD['left'] = dataFrame[dataFrame.left == leftLabel].leftWeight.sum()
            if i == 0:
                myD['bottom'] = 0
                myD['top'] = myD['left']
            else:
                myD['bottom'] = leftWidths[leftLabels[i - 1]]['top'] + 0.02 * dataFrame.leftWeight.sum()
                myD['top'] = myD['bottom'] + myD['left']
                topEdge = myD['top']
            leftWidths[leftLabel] = myD

        # Determine positions of right label patches and total widths
        rightWidths = defaultdict()
        for i, rightLabel in enumerate(rightLabels):
            myD = {}
            myD['right'] = dataFrame[dataFrame.right == rightLabel].rightWeight.sum()
            if i == 0:
                myD['bottom'] = 0
                myD['top'] = myD['right']
            else:
                myD['bottom'] = rightWidths[rightLabels[i - 1]]['top'] + 0.02 * dataFrame.rightWeight.sum()
                myD['top'] = myD['bottom'] + myD['right']
                topEdge = myD['top']
            rightWidths[rightLabel] = myD

        # Total vertical extent of diagram
        xMax = topEdge / aspect

        # Draw vertical bars on left and right of each  label's section & print label
        for leftLabel in leftLabels:
            plt.fill_between(
                [-0.02 * xMax, 0],
                2 * [leftWidths[leftLabel]['bottom']],
                2 * [leftWidths[leftLabel]['bottom'] + leftWidths[leftLabel]['left']],
                color=colorDict[leftLabel],
                alpha=0.99
            )
            plt.text(
                -0.05 * xMax,
                leftWidths[leftLabel]['bottom'] + 0.5 * leftWidths[leftLabel]['left'],
                leftLabel,
                {'ha': 'right', 'va': 'center'},
                fontsize=fontsize
            )
        for rightLabel in rightLabels:
            plt.fill_between(
                [xMax, 1.02 * xMax], 2 * [rightWidths[rightLabel]['bottom']],
                2 * [rightWidths[rightLabel]['bottom'] + rightWidths[rightLabel]['right']],
                color=colorDict[rightLabel],
                alpha=0.99
            )
            plt.text(
                1.05 * xMax,
                rightWidths[rightLabel]['bottom'] + 0.5 * rightWidths[rightLabel]['right'],
                rightLabel,
                {'ha': 'left', 'va': 'center'},
                fontsize=fontsize
            )

        # Plot strips
        for leftLabel in leftLabels:
            for rightLabel in rightLabels:
                labelColor = leftLabel
                if rightColor:
                    labelColor = rightLabel
                if len(dataFrame[(dataFrame.left == leftLabel) & (dataFrame.right == rightLabel)]) > 0:
                    # Create array of y values for each strip, half at left value,
                    # half at right, convolve
                    ys_d = np.array(50 * [leftWidths[leftLabel]['bottom']] + 50 * [rightWidths[rightLabel]['bottom']])
                    ys_d = np.convolve(ys_d, 0.05 * np.ones(20), mode='valid')
                    ys_d = np.convolve(ys_d, 0.05 * np.ones(20), mode='valid')
                    ys_u = np.array(50 * [leftWidths[leftLabel]['bottom'] + ns_l[leftLabel][rightLabel]] + 50 * [rightWidths[rightLabel]['bottom'] + ns_r[leftLabel][rightLabel]])
                    ys_u = np.convolve(ys_u, 0.05 * np.ones(20), mode='valid')
                    ys_u = np.convolve(ys_u, 0.05 * np.ones(20), mode='valid')

                    # Update bottom edges at each label so next strip starts at the right place
                    leftWidths[leftLabel]['bottom'] += ns_l[leftLabel][rightLabel]
                    rightWidths[rightLabel]['bottom'] += ns_r[leftLabel][rightLabel]
                    plt.fill_between(
                        np.linspace(0, xMax, len(ys_d)), ys_d, ys_u, alpha=0.65,
                        color=colorDict[labelColor]
                    )
        plt.xlim([0, xMax])
        plt.gca().axis('off')


def check_data_matches_labels(labels, data, side):
    if len(labels > 0):
        if isinstance(data, list):
            data = set(data)
        if isinstance(data, pd.Series):
            data = set(data.unique().tolist())
        if isinstance(labels, list):
            labels = set(labels)
        if labels != data:
            msg = "\n"
            if len(labels) <= 20:
                msg = "Labels: " + ",".join(labels) + "\n"
            if len(data) < 20:
                msg += "Data: " + ",".join(data)
            raise LabelMismatch('{0} labels and data do not match.{1}'.format(side, msg))




values_flows = {'ini1':1000, 'ini2':2000, 'mid1': 500, 'mid2': 2500, 'out1': 1000, 'out2':1500, 'out3':500}
connect = [('ini1', 'mid1'),
           ('ini1', 'mid2'),
           ('ini2', 'mid2'),
           ('mid2', 'out2'),
           ('mid1', 'out1'),
           ('mid2', 'out3')]
mysankey = Sankey()
mysankey.plot_sankey(values_flows, connect, title='', show=True)