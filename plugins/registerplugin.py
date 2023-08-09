# coding:utf-8
import traceback
from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection

from basic_input_plugin import *
from container_plugin import *
from date_time_plugin import *
from navigation_plugin import *
from status_info_plugin import *
from text_plugin import *
from view_plugin import *
from toolbar_plugin import *


# basic input plugins
QPyDesignerCustomWidgetCollection.addCustomWidget(CheckBoxPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(ComboBoxPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(EditableComboBoxPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(HyperlinkButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(DropDownPushButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(PushButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(PrimaryPushButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(SplitPushButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(ToolButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(DropDownToolButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(SplitToolButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(RadioButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(SwitchButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(ToggleButtonPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(SliderPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(IconWidgetPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(PixmapLabelPlugin())

# container plugins
QPyDesignerCustomWidgetCollection.addCustomWidget(ScrollAreaPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(SmoothScrollAreaPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(SingleDirectionScrollAreaPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(OpacityAniStackedWidgetPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(PopUpAniStackedWidgetPlugin())

# date time plugins
QPyDesignerCustomWidgetCollection.addCustomWidget(DatePickerPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(ZhDatePickerPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(TimePickerPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(AMTimePickerPlugin())

# navigation plugins
QPyDesignerCustomWidgetCollection.addCustomWidget(NavigationInterfacePlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(NavigationPanelPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(PivotPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(SegmentedWidgetPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(TabBarPlugin())

# status info plugins
QPyDesignerCustomWidgetCollection.addCustomWidget(InfoBarPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(IndeterminateProgressBarPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(ProgressBarPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(ProgressRingPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(StateToolTipPlugin())

# text plugins
QPyDesignerCustomWidgetCollection.addCustomWidget(LineEditPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(DateEditPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(DateTimeEditPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(DoubleSpinBoxPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(PlainTextEditPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(SpinBoxPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(TextEditPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(TimeEditPlugin())

# view plugins
QPyDesignerCustomWidgetCollection.addCustomWidget(ListWidgetPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(ListViewPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(TableWidgetPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(TableViewPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(TreeWidgetPlugin())
QPyDesignerCustomWidgetCollection.addCustomWidget(TreeViewPlugin())

# tool bar plugin
QPyDesignerCustomWidgetCollection.addCustomWidget(ToolBarPlugin())
