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
              "data": "\"\"\"\n===============================================\nProgrammatically controlling subplot adjustment\n===============================================\n\n.. note::\n\n    This example is primarily intended to show some advanced concepts in\n    Matplotlib.\n\n    If you are only looking for having enough space for your labels, it is\n    almost always simpler and good enough to either set the subplot parameters\n    manually using `.Figure.subplots_adjust`, or use one of the automatic\n    layout mechanisms\n    (:doc:`/tutorials/intermediate/constrainedlayout_guide` or\n    :doc:`/tutorials/intermediate/tight_layout_guide`).\n\nThis example describes a user-defined way to read out Artist sizes and\nset the subplot parameters accordingly. Its main purpose is to illustrate\nsome advanced concepts like reading out text positions, working with\nbounding boxes and transforms and using\n:ref:`events <event-handling-tutorial>`. But it can also serve as a starting\npoint if you want to automate the layouting and need more flexibility than\ntight layout and constrained layout.\n\nBelow, we collect the bounding boxes of all y-labels and move the left border\nof the subplot to the right so that it leaves enough room for the union of all\nthe bounding boxes.\n\nThere's one catch with calculating text bounding boxes:\nQuerying the text bounding boxes (`.Text.get_window_extent`) needs a\nrenderer (`.RendererBase` instance), to calculate the text size. This renderer\nis only available after the figure has been drawn (`.Figure.draw`).\n\nA solution to this is putting the adjustment logic in a draw callback.\nThis function is executed after the figure has been drawn. It can now check\nif the subplot leaves enough room for the text. If not, the subplot parameters\nare updated and second draw is triggered.\n\"\"\""
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
                "value": "matplotlib",
                "reference": {
                  "module": "matplotlib",
                  "version": "3.5.0",
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
                  "version": "3.5.0",
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
              "data": "transforms"
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
              "data": "mtransforms"
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
            "type": "nb",
            "link": {
              "type": "str",
              "data": "range"
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
              "data": "10"
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
              "data": "set_yticks"
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
              "data": "["
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
              "data": "5"
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
              "data": "7"
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
              "data": "labels"
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
              "data": "["
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
              "data": "really, really, really"
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
              "data": "long"
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
              "data": "labels"
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
              "data": "]"
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
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "bboxes"
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
              "data": "    "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "for"
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
              "data": "label"
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
              "data": "in"
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
              "data": "get_yticklabels"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# Bounding box in pixels"
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
              "data": "bbox_px"
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
              "data": "label"
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
              "data": "get_window_extent"
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
              "data": "        "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# Transform to relative figure coordinates. This is the inverse of"
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
              "data": "# transFigure."
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
              "data": "bbox_fig"
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
              "data": "bbox_px"
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
              "data": "transformed"
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
              "data": "fig"
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
              "data": "transFigure"
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
              "data": "inverted"
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
              "data": "bboxes"
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
              "data": "append"
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
              "data": "bbox_fig"
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
              "data": "    "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# the bbox that bounds all the bboxes, again in relative figure coords"
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
              "data": "bbox"
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
              "data": "mtransforms"
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
              "data": "Bbox"
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
              "data": "union"
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
              "data": "bboxes"
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
              "data": "    "
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
              "data": "fig"
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
              "data": "subplotpars"
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
              "data": "left"
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
              "data": "<"
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
              "data": "bbox"
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
              "data": "width"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# Move the subplot left edge more to the right"
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
              "data": "fig"
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
              "data": "subplots_adjust"
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
              "data": "left"
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
              "data": "1.1"
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
              "data": "bbox"
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
              "data": "width"
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
              "data": "  "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# pad a little"
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
              "data": "fig"
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
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#############################################################################"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# .. admonition:: References"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    The use of the following functions, methods, classes and modules is shown"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    in this example:"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.artist.Artist.get_window_extent`"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.transforms.Bbox`"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.transforms.BboxBase.transformed`"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.transforms.BboxBase.union`"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.transforms.Transform.inverted`"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.figure.Figure.subplots_adjust`"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.figure.SubplotParams`"
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
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.backend_bases.FigureCanvasBase.mpl_connect`"
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
        "ce_status": "execed"
      }
    },
    {
      "type": "Fig",
      "data": {
        "value": "ex-auto_subplots_adjust.py-0.png"
      }
    }
  ],
  "title": null
}