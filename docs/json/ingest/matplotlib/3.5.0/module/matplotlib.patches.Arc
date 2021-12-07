{
  "_content": {
    "Attributes": {
      "children": [],
      "title": null
    },
    "Extended Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Due to internal optimizations, there are certain restrictions on using Arc:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BulletList",
          "data": {
            "value": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The arc cannot be filled."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "BulletList",
          "data": {
            "value": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The arc must be used in an "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": [
                          "~.axes.Axes"
                        ],
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " instance. It can not be added   directly to a "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": [
                          ".Figure"
                        ],
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " because it is optimized to only render the   segments that are inside the axes bounding box with high resolution."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        }
      ],
      "title": null
    },
    "Methods": {
      "children": [],
      "title": null
    },
    "Notes": {
      "children": [],
      "title": null
    },
    "Other Parameters": {
      "children": [],
      "title": null
    },
    "Parameters": {
      "children": [],
      "title": null
    },
    "Raises": {
      "children": [],
      "title": null
    },
    "Receives": {
      "children": [],
      "title": null
    },
    "Returns": {
      "children": [],
      "title": null
    },
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "An elliptical arc, i.e. a segment of an ellipse."
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Warnings": {
      "children": [],
      "title": null
    },
    "Warns": {
      "children": [],
      "title": null
    },
    "Yields": {
      "children": [],
      "title": null
    }
  },
  "refs": [],
  "ordered_sections": [
    "Summary",
    "Extended Summary"
  ],
  "item_file": "/matplotlib/patches.py",
  "item_line": 1843,
  "item_type": "<class 'type'>",
  "aliases": [
    "matplotlib.patches.Arc"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "3.5.0",
  "signature": "Arc(xy, width, height, angle=0.0, theta1=0.0, theta2=360.0, **kwargs)",
  "references": null,
  "logo": "logo.png",
  "qa": "matplotlib.patches.Arc",
  "arbitrary": []
}