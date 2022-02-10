{
  "children": [
    {
      "type": "Code2",
      "data": {
        "entries": [
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"\n===========\nPath Editor\n===========\n\nSharing events across GUIs.\n\nThis example demonstrates a cross-GUI application using Matplotlib event\nhandling to interact with and modify objects on the canvas.\n\n.. note::\n    This example exercises the interactive capabilities of Matplotlib, and this\n    will not appear in the static documentation. Please run this code on your\n    machine to see the interactivity.\n\n    You can copy and paste individual parts, or download the entire example\n    using the link at the bottom of the page.\n\"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "import"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "Link",
              "data": {
                "value": "numpy",
                "reference": {
                  "module": "numpy",
                  "version": "1.22.1",
                  "kind": "module",
                  "path": "numpy"
                },
                "kind": "module",
                "exists": true
              }
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "as"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "np"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "from"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "Link",
              "data": {
                "value": "matplotlib",
                "reference": {
                  "module": "matplotlib",
                  "version": "3.5.1",
                  "kind": "module",
                  "path": "matplotlib"
                },
                "kind": "module",
                "exists": true
              }
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "backend_bases"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "import"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "MouseButton"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "from"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "Link",
              "data": {
                "value": "matplotlib",
                "reference": {
                  "module": "matplotlib",
                  "version": "3.5.1",
                  "kind": "module",
                  "path": "matplotlib"
                },
                "kind": "module",
                "exists": true
              }
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "path"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "import"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "from"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "Link",
              "data": {
                "value": "matplotlib",
                "reference": {
                  "module": "matplotlib",
                  "version": "3.5.1",
                  "kind": "module",
                  "path": "matplotlib"
                },
                "kind": "module",
                "exists": true
              }
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "patches"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "import"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "PathPatch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "import"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "Link",
              "data": {
                "value": "matplotlib",
                "reference": {
                  "module": "matplotlib",
                  "version": "3.5.1",
                  "kind": "module",
                  "path": "matplotlib"
                },
                "kind": "module",
                "exists": true
              }
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "pyplot"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "as"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "plt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "fig"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "plt"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "subplots"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathdata"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "MOVETO"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "1.58"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "2.57"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "CURVE4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.35"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "1.1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "CURVE4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "1.75"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "2.0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "CURVE4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.375"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "2.0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "LINETO"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.85"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "1.15"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "CURVE4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "2.2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "3.2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "CURVE4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "3"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.05"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "CURVE4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "2.0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.5"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "CLOSEPOLY"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "1.58"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "2.57"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "codes"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "verts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nb",
            "link": {
              "type": "str",
              "data": "zip"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathdata"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "path"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "Path"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "verts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "codes"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "patch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "PathPatch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "path"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "facecolor"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "green"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "edgecolor"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "yellow"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "alpha"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.5"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "add_patch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "patch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "class"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nc",
            "link": {
              "type": "str",
              "data": "PathInteractor"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"\n    An path editor.\n\n    Press 't' to toggle vertex markers on and off.  When vertex markers are on,\n    they can be dragged with the mouse.\n    \"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "showverts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "True"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "epsilon"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "5"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "  "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# max pixel distance to count as a vertex hit"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "def"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "fm",
            "link": {
              "type": "str",
              "data": "__init__"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "axes"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "figure"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "set_animated"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "True"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nb",
            "link": {
              "type": "str",
              "data": "zip"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "get_path"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "vertices"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "line"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "plot"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "marker"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "o"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "markerfacecolor"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "r"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "animated"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "True"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "_ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "None"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "  "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# the active vertex"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "mpl_connect"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "draw_event"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "on_draw"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "mpl_connect"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "button_press_event"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "on_button_press"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "mpl_connect"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "key_press_event"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "on_key_press"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "mpl_connect"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "button_release_event"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "on_button_release"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "mpl_connect"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "motion_notify_event"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "on_mouse_move"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "def"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nf",
            "link": {
              "type": "str",
              "data": "get_ind_under_point"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"\n        Return the index of the point closest to the event position or *None*\n        if no point is within ``self.epsilon`` to the event position.\n        \"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# display coords"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xy"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "np"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "asarray"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "get_path"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "vertices"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xyt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "get_transform"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "transform"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xy"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "yt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xyt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xyt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "d"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "np"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "sqrt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "yt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "d"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "argmin"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "if"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "d"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": ">"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "epsilon"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "None"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "return"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "def"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nf",
            "link": {
              "type": "str",
              "data": "on_draw"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"Callback for draws.\"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "background"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "copy_from_bbox"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "bbox"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "draw_artist"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "draw_artist"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "line"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "blit"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "bbox"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "def"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nf",
            "link": {
              "type": "str",
              "data": "on_button_press"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"Callback for mouse button presses.\"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "if"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "inaxes"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "is"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "None"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "                "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "or"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "button"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "!="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "MouseButton"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "LEFT"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "                "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "or"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "not"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "showverts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "return"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "_ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "get_ind_under_point"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "def"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nf",
            "link": {
              "type": "str",
              "data": "on_button_release"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"Callback for mouse button releases.\"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "if"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "button"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "!="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "MouseButton"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "LEFT"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "                "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "or"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "not"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "showverts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "return"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "_ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "None"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "def"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nf",
            "link": {
              "type": "str",
              "data": "on_key_press"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"Callback for key presses.\"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "if"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "not"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "inaxes"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "return"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "if"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "key"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "=="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "t"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "showverts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "not"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "showverts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "line"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "set_visible"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "showverts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "if"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "not"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "showverts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "                "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "_ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "None"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "draw"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "def"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nf",
            "link": {
              "type": "str",
              "data": "on_mouse_move"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"Callback for mouse movements.\"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "if"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "_ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "is"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "None"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "                "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "or"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "inaxes"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "is"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "None"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "                "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "or"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "button"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "!="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "MouseButton"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "LEFT"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "                "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "or"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "not"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "showverts"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "return"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "vertices"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "get_path"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "vertices"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "vertices"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "_ind"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xdata"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "event"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ydata"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "line"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "set_data"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "nb",
            "link": {
              "type": "str",
              "data": "zip"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "vertices"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "restore_region"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "background"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "draw_artist"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "pathpatch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "draw_artist"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "line"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "        "
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "canvas"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "blit"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "bp",
            "link": {
              "type": "str",
              "data": "self"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "bbox"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "interactor"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "PathInteractor"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "patch"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "set_title"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "drag vertices to update path"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "set_xlim"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "3"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "set_ylim"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "-"
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "3"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "plt"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "show"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          }
        ],
        "out": "",
        "ce_status": "None"
      }
    }
  ],
  "title": null
}