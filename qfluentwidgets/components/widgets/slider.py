# coding:utf-8
from PySide6.QtCore import QSize, Qt, Signal, QPoint, QRectF
from PySide6.QtGui import QColor, QMouseEvent, QPainter, QPainterPath
from PySide6.QtWidgets import (QProxyStyle, QSlider, QStyle, QStyleOptionSlider,
                             QWidget)

from ...common.style_sheet import FluentStyleSheet
from ...common.overload import singledispatchmethod


class Slider(QSlider):
    """ A slider can be clicked """

    clicked = Signal(int)

    @singledispatchmethod
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        FluentStyleSheet.SLIDER.apply(self)

    @__init__.register
    def _(self, orientation: Qt.Orientation, parent: QWidget = None):
        super().__init__(orientation, parent=parent)
        FluentStyleSheet.SLIDER.apply(self)

    def mousePressEvent(self, e: QMouseEvent):
        super().mousePressEvent(e)

        if self.orientation() == Qt.Horizontal:
            value = int(e.pos().x() / self.width() * self.maximum())
        else:
            value = int((self.height()-e.pos().y()) /
                        self.height() * self.maximum())

        self.setValue(value)
        self.clicked.emit(self.value())


class HollowHandleStyle(QProxyStyle):
    """ Hollow handle style """

    def __init__(self, config: dict = None):
        """
        Parameters
        ----------
        config: dict
            style config
        """
        super().__init__()
        self.config = {
            "groove.height": 3,
            "sub-page.color": QColor(255, 255, 255),
            "add-page.color": QColor(255, 255, 255, 64),
            "handle.color": QColor(255, 255, 255),
            "handle.ring-width": 4,
            "handle.hollow-radius": 6,
            "handle.margin": 4
        }
        config = config if config else {}
        self.config.update(config)

        # get handle size
        w = self.config["handle.margin"]+self.config["handle.ring-width"] + \
            self.config["handle.hollow-radius"]
        self.config["handle.size"] = QSize(2*w, 2*w)

    def subControlRect(self, cc: QStyle.ComplexControl, opt: QStyleOptionSlider, sc: QStyle.SubControl, widget: QSlider):
        """ get the rectangular area occupied by the sub control """
        if cc != self.ComplexControl.CC_Slider or widget.orientation() != Qt.Horizontal \
                or sc == self.SubControl.SC_SliderTickmarks:
            return super().subControlRect(cc, opt, sc, widget)

        rect = widget.rect()

        if sc == self.SubControl.SC_SliderGroove:
            h = self.config["groove.height"]
            grooveRect = QRectF(0, (rect.height()-h)//2, rect.width(), h)
            return grooveRect.toRect()

        elif sc == self.SubControl.SC_SliderHandle:
            size = self.config["handle.size"]
            x = self.sliderPositionFromValue(
                widget.minimum(), widget.maximum(), widget.value(), rect.width())

            # solve the situation that the handle runs out of slider
            x *= (rect.width()-size.width())/rect.width()
            sliderRect = QRectF(x, 0, size.width(), size.height())
            return sliderRect.toRect()

    def drawComplexControl(self, cc: QStyle.ComplexControl, opt: QStyleOptionSlider, painter: QPainter, widget: QSlider):
        """ draw sub control """
        if cc != self.ComplexControl.CC_Slider or widget.orientation() != Qt.Horizontal:
            return super().drawComplexControl(cc, opt, painter, widget)

        grooveRect = self.subControlRect(cc, opt, self.SubControl.SC_SliderGroove, widget)
        handleRect = self.subControlRect(cc, opt, self.SubControl.SC_SliderHandle, widget)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # paint groove
        painter.save()
        painter.translate(grooveRect.topLeft())

        # paint the crossed part
        w = handleRect.x()-grooveRect.x()
        h = self.config['groove.height']
        painter.setBrush(self.config["sub-page.color"])
        painter.drawRect(0, 0, w, h)

        # paint the uncrossed part
        x = w+self.config['handle.size'].width()
        painter.setBrush(self.config["add-page.color"])
        painter.drawRect(x, 0, grooveRect.width()-w, h)
        painter.restore()

        # paint handle
        ringWidth = self.config["handle.ring-width"]
        hollowRadius = self.config["handle.hollow-radius"]
        radius = ringWidth + hollowRadius

        path = QPainterPath()
        path.moveTo(0, 0)
        center = handleRect.center() + QPoint(1, 1)
        path.addEllipse(center, radius, radius)
        path.addEllipse(center, hollowRadius, hollowRadius)

        handleColor = self.config["handle.color"]  # type:QColor
        handleColor.setAlpha(255 if opt.activeSubControls !=
                             self.SubControl.SC_SliderHandle else 153)
        painter.setBrush(handleColor)
        painter.drawPath(path)

        # press handle
        if widget.isSliderDown():
            handleColor.setAlpha(255)
            painter.setBrush(handleColor)
            painter.drawEllipse(handleRect)
