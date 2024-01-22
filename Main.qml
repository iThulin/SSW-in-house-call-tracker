import QtQuick
import QtQuick.Controls.basic

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Hello World"

    Text {
        anchors.centerIn: parent
        text: "Hello World"
        font.pixelSize: 24
    }
}