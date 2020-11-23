# qmlunfuck

Qt has introduced a new means of exposing C++ objects to QML: The `QML_ELEMENT` macro, combined with the `qmltyperegistrar` tool. However, Qt Creator doesn't seem to have gotten the message - it will present import errors in your QML editor, even when the project builds just fine.

As a workaround, I present `qmlunfuck`. `qmlunfuck` generates C++ code that uses the older style of type registration, registering all your objects in a way that Qt Creator is capable of recognizing.

## Adding to Your Project

1. Make sure you've set up `qmltypes` correctly in your qmake file:
   - `CONFIG += qmltypes` is present
   - You're setting `QML_IMPORT_NAME` and `QML_IMPORT_MAJOR_VERSION` correctly.

2. Clone `qmlunfuck` into a subdirectory of your project.

3. Add the path to `qmlunfuck` to your `$$QMAKEFEATURES` project variable.

4. Add `CONFIG += qmlunfuck` to your project.

5. Run `qmake`, and build your project! Qt Creator should stop complaining and recognize properly annotated C++ objects in QML.

### Example QMake Config

Assuming you cloned `qmlunfuck` to a subdirectory of your project called "qmlunfuck", your project's `.pro` file should have lines like these:

```qmake
QMAKEFEATURES += $$PWD/qmlunfuck
CONFIG += qmltypes qmlunfuck

QML_IMPORT_NAME = com.example.myproject
QML_IMPORT_MAJOR_VERSION = 1
```
