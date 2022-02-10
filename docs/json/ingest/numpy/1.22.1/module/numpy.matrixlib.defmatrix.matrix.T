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
                  "value": "Does "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "not"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " conjugate!  For the complex conjugate transpose, use "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    ".H"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "."
                }
              }
            ],
            "inner": []
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
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "None",
            "type_": "",
            "desc": []
          }
        }
      ],
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
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "ret",
            "type_": "matrix object",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The (non-conjugated) transpose of the matrix."
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
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Returns the transpose of the matrix."
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
  "refs": [
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.matrix"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters",
    "Returns",
    "See Also",
    "Examples"
  ],
  "item_file": "/numpy/matrixlib/defmatrix.py",
  "item_line": 935,
  "item_type": "<class 'function'>",
  "aliases": [
    "numpy.matrix.getT"
  ],
  "example_section_data": {
    "children": [
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "m"
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
                "type": "Link",
                "data": {
                  "value": "matrix",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.matrix"
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
                "data": "[1, 2; 3, 4]"
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
                "data": "m"
              }
            }
          ],
          "out": "matrix([[1, 2],\n        [3, 4]])",
          "ce_status": "execed"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "m"
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
                "data": "getT"
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
            }
          ],
          "out": "matrix([[1, 3],\n        [2, 4]])",
          "ce_status": "execed"
        }
      }
    ],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "getH",
        "ref": null,
        "exists": null
      },
      "descriptions": [],
      "type": null
    },
    {
      "name": {
        "name": "transpose",
        "ref": "numpy.transpose",
        "exists": true
      },
      "descriptions": [],
      "type": null
    }
  ],
  "version": "1.22.1",
  "signature": "T(self)",
  "references": null,
  "logo": "logo.png",
  "qa": "numpy.matrixlib.defmatrix.matrix.T",
  "arbitrary": []
}