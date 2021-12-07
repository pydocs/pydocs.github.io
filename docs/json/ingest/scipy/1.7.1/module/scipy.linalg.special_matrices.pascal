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
                  "value": "The Pascal matrix is a matrix containing the binomial coefficients as its elements."
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
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "See https://en.wikipedia.org/wiki/Pascal_matrix for more information about Pascal matrices."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Admonition",
          "data": {
            "kind": "versionadded",
            "title": "TODO",
            "children": [
              {
                "inline": [
                  {
                    "type": "Words",
                    "data": {
                      "value": "0.11.0 "
                    }
                  }
                ],
                "inner": []
              }
            ]
          }
        }
      ],
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
            "param": "n",
            "type_": "int",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The size of the matrix to create; that is, the result is an n x n matrix."
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
          "type": "Param",
          "data": {
            "param": "kind",
            "type_": "str, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Must be one of 'symmetric', 'lower', or 'upper'. Default is 'symmetric'."
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
          "type": "Param",
          "data": {
            "param": "exact",
            "type_": "bool, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "exact",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "exact"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is True, the result is either an array of type numpy.uint64 (if n < 35) or an object array of Python long integers. If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "exact",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "exact"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is False, the coefficients in the matrix are computed using "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": [
                          "scipy.special.comb"
                        ],
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " with "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": [
                          "exact=False"
                        ],
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ". The result will be a floating point array, and the values in the array will not be the exact coefficients, but this version is much faster than "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": [
                          "exact=True"
                        ],
                        "domain": null,
                        "role": null
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
            ]
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
            "param": "p",
            "type_": "(n, n) ndarray",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The Pascal matrix."
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
                  "value": "Returns the n x n Pascal matrix."
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
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.linalg.special_matrices.pascal"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.sparse.linalg"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.special"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.special._basic.comb"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters",
    "Returns",
    "See Also",
    "Notes",
    "Examples"
  ],
  "item_file": "/scipy/linalg/special_matrices.py",
  "item_line": 776,
  "item_type": "<class 'function'>",
  "aliases": [
    "scipy.signal.lti_conversion.linalg.pascal"
  ],
  "example_section_data": {
    "children": [
      {
        "type": "Code2",
        "data": {
          "entries": [
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
                  "value": "scipy",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy"
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
                "type": "Link",
                "data": {
                  "value": "linalg",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.sparse.linalg"
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
                "type": "Link",
                "data": {
                  "value": "pascal",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.linalg.special_matrices.pascal"
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
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "pascal",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.linalg.special_matrices.pascal"
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
            }
          ],
          "out": "array([[ 1,  1,  1,  1],\n       [ 1,  2,  3,  4],\n       [ 1,  3,  6, 10],\n       [ 1,  4, 10, 20]], dtype=uint64)",
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
                "type": "Link",
                "data": {
                  "value": "pascal",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.linalg.special_matrices.pascal"
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
                "data": "kind"
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
                "data": "lower"
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
            }
          ],
          "out": "array([[1, 0, 0, 0],\n       [1, 1, 0, 0],\n       [1, 2, 1, 0],\n       [1, 3, 3, 1]], dtype=uint64)",
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
                "type": "Link",
                "data": {
                  "value": "pascal",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.linalg.special_matrices.pascal"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "50"
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
                "data": "["
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
                "data": "1"
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
            }
          ],
          "out": "25477612258980856902730428600",
          "ce_status": "execed"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
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
                  "value": "scipy",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy"
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
                "type": "Link",
                "data": {
                  "value": "special",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.special"
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
                "type": "Link",
                "data": {
                  "value": "comb",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.special._basic.comb"
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
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "comb",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.special._basic.comb"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "98"
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
                "data": "49"
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
                "data": "exact"
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
            }
          ],
          "out": "25477612258980856902730428600",
          "ce_status": "execed"
        }
      }
    ],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "invpascal",
        "ref": "scipy.linalg.special_matrices.invpascal",
        "exists": true
      },
      "descriptions": [],
      "type": null
    }
  ],
  "version": "1.7.1",
  "signature": "pascal(n, kind='symmetric', exact=True)",
  "references": null,
  "logo": "logo.png",
  "qa": "scipy.linalg.special_matrices.pascal",
  "arbitrary": []
}