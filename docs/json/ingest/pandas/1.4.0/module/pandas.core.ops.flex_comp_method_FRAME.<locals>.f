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
                  "value": "Among flexible wrappers ("
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "eq",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "ne",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "le",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "lt",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "ge",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "gt",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ") to comparison operators."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Equivalent to "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "==",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "!=",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "<=",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "<",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": ">=",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": ">",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " with support to choose axis (rows or columns) and level for comparison."
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
                  "value": "Mismatched indices will be unioned together. "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "NaN",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.errors.IntCastingNaNError"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " values are considered different (i.e. "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "NaN",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.errors.IntCastingNaNError"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " != "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "NaN",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.errors.IntCastingNaNError"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ")."
                }
              }
            ],
            "inner": []
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
            "param": "other",
            "type_": "scalar, sequence, Series, or DataFrame",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Any single or multiple element data structure, or list-like object."
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
            "param": "axis",
            "type_": "{0 or 'index', 1 or 'columns'}, default 'columns'",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Whether to compare by the index (0 or 'index') or columns (1 or 'columns')."
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
            "param": "level",
            "type_": "int or label",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Broadcast across a level, matching Index values on the passed MultiIndex level."
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
            "param": "",
            "type_": "DataFrame of bool",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Result of the comparison."
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
                  "value": "Get Greater than or equal to of dataframe and other, element-wise (binary operator "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "ge",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ")."
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
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.core.frame.DataFrame"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.errors.IntCastingNaNError"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.core.series.Series"
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
  "item_file": "/pandas/core/ops/__init__.py",
  "item_line": 464,
  "item_type": "<class 'function'>",
  "aliases": [
    "pandas.DataFrame.eq",
    "pandas.DataFrame.ne",
    "pandas.DataFrame.lt",
    "pandas.DataFrame.gt",
    "pandas.DataFrame.le",
    "pandas.DataFrame.ge"
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
                "data": "df"
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
                "data": "pd"
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
                  "value": "DataFrame",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.frame.DataFrame"
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
              "type": "",
              "link": {
                "type": "str",
                "data": "{"
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
                "data": "cost"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "250"
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
                "data": "150"
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
                "data": "100"
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
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "                   "
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
                "data": "revenue"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "100"
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
                "data": "250"
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
                "data": "300"
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
                "data": "}"
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
                "data": "                  "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "index"
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
                "data": "A"
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
                "data": "B"
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
                "data": "C"
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
                "data": "df"
              }
            }
          ],
          "out": "   cost  revenue\nA   250      100\nB   150      250\nC   100      300",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Comparison with a scalar, using either the operator or method:"
              }
            }
          ],
          "inner": []
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
                "data": "df"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "100"
              }
            }
          ],
          "out": "    cost  revenue\nA  False     True\nB  False    False\nC   True    False",
          "ce_status": "compiled"
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
                "data": "df"
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
                "data": "eq"
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
                "data": "100"
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
          "out": "    cost  revenue\nA  False     True\nB  False    False\nC   True    False",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "When "
              }
            },
            {
              "type": "Link",
              "data": {
                "value": "other",
                "reference": {
                  "module": "pandas",
                  "version": "1.4.0",
                  "kind": "module",
                  "path": "pandas.io.formats.css.CSSResolver._update_other_units"
                },
                "kind": "module",
                "exists": true
              }
            },
            {
              "type": "Words",
              "data": {
                "value": " is a "
              }
            },
            {
              "type": "Link",
              "data": {
                "value": "Series",
                "reference": {
                  "module": "pandas",
                  "version": "1.4.0",
                  "kind": "module",
                  "path": "pandas.core.series.Series"
                },
                "kind": "module",
                "exists": true
              }
            },
            {
              "type": "Words",
              "data": {
                "value": ", the columns of a DataFrame are aligned with the index of "
              }
            },
            {
              "type": "Link",
              "data": {
                "value": "other",
                "reference": {
                  "module": "pandas",
                  "version": "1.4.0",
                  "kind": "module",
                  "path": "pandas.io.formats.css.CSSResolver._update_other_units"
                },
                "kind": "module",
                "exists": true
              }
            },
            {
              "type": "Words",
              "data": {
                "value": " and broadcast:"
              }
            }
          ],
          "inner": []
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
                "data": "df"
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
                "data": "pd"
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
                  "value": "Series",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.series.Series"
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
                "data": "100"
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
                "data": "250"
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
                "data": "index"
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
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "cost"
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
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
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "revenue"
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
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
            }
          ],
          "out": "    cost  revenue\nA   True     True\nB   True    False\nC  False     True",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Use the method to control the broadcast axis:"
              }
            }
          ],
          "inner": []
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
                "data": "df"
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
                "data": "ne"
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
                "data": "pd"
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
                  "value": "Series",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.series.Series"
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
                "data": "100"
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
                "data": "300"
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
                "data": "index"
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
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "A"
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
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
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "D"
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
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
                "data": "axis"
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
                "data": "index"
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
          "out": "   cost  revenue\nA  True    False\nB  True     True\nC  True     True\nD  True     True",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "When comparing to an arbitrary sequence, the number of columns must match the number elements in "
              }
            },
            {
              "type": "Link",
              "data": {
                "value": "other",
                "reference": {
                  "module": "pandas",
                  "version": "1.4.0",
                  "kind": "module",
                  "path": "pandas.io.formats.css.CSSResolver._update_other_units"
                },
                "kind": "module",
                "exists": true
              }
            },
            {
              "type": "Words",
              "data": {
                "value": ":"
              }
            }
          ],
          "inner": []
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
                "data": "df"
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
                "data": "250"
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
                "data": "100"
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
          "out": "    cost  revenue\nA   True     True\nB  False    False\nC  False    False",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Use the method to control the axis:"
              }
            }
          ],
          "inner": []
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
                "data": "df"
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
                "data": "eq"
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
                "data": "250"
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
                "data": "250"
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
                "data": "100"
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
                "data": "axis"
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
                "data": "index"
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
          "out": "    cost  revenue\nA   True    False\nB  False     True\nC   True    False",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compare to a DataFrame of different shape."
              }
            }
          ],
          "inner": []
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
                "data": "other"
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
                "data": "pd"
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
                  "value": "DataFrame",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.frame.DataFrame"
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
              "type": "",
              "link": {
                "type": "str",
                "data": "{"
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
                "data": "revenue"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "300"
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
                "data": "250"
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
                "data": "100"
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
                "data": "150"
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
                "data": "}"
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
                "data": "                     "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "index"
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
                "data": "A"
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
                "data": "B"
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
                "data": "C"
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
                "data": "D"
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
                "data": "other"
              }
            }
          ],
          "out": "   revenue\nA      300\nB      250\nC      100\nD      150",
          "ce_status": "compiled"
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
                "data": "df"
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
                "data": "gt"
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
                "data": "other"
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
          "out": "    cost  revenue\nA  False    False\nB  False    False\nC  False     True\nD  False    False",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compare to a MultiIndex by level."
              }
            }
          ],
          "inner": []
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
                "data": "df_multindex"
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
                "data": "pd"
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
                  "value": "DataFrame",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.frame.DataFrame"
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
              "type": "",
              "link": {
                "type": "str",
                "data": "{"
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
                "data": "cost"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "250"
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
                "data": "150"
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
                "data": "100"
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
                "data": "150"
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
                "data": "300"
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
                "data": "220"
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
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "                             "
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
                "data": "revenue"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "100"
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
                "data": "250"
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
                "data": "300"
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
                "data": "200"
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
                "data": "175"
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
                "data": "225"
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
                "data": "}"
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
                "data": "                            "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "index"
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
                "data": "Q1"
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
                "data": "Q1"
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
                "data": "Q1"
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
                "data": "Q2"
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
                "data": "Q2"
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
                "data": "Q2"
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
                "data": "                                   "
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
                "data": "A"
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
                "data": "B"
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
                "data": "C"
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
                "data": "A"
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
                "data": "B"
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
                "data": "C"
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
                "data": "df_multindex"
              }
            }
          ],
          "out": "      cost  revenue\nQ1 A   250      100\n   B   150      250\n   C   100      300\nQ2 A   150      200\n   B   300      175\n   C   220      225",
          "ce_status": "compiled"
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
                "data": "df"
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
                "data": "le"
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
                "data": "df_multindex"
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
                "data": "level"
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
                "data": ")"
              }
            }
          ],
          "out": "       cost  revenue\nQ1 A   True     True\n   B   True     True\n   C   True     True\nQ2 A  False     True\n   B   True    False\n   C   True    False",
          "ce_status": "compiled"
        }
      }
    ],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "DataFrame.eq",
        "ref": null,
        "exists": null
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compare DataFrames for equality elementwise."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "DataFrame.ge",
        "ref": null,
        "exists": null
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compare DataFrames for greater than inequality or equality elementwise."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "DataFrame.gt",
        "ref": null,
        "exists": null
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compare DataFrames for strictly greater than inequality elementwise."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "DataFrame.le",
        "ref": null,
        "exists": null
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compare DataFrames for less than inequality or equality elementwise."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "DataFrame.lt",
        "ref": null,
        "exists": null
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compare DataFrames for strictly less than inequality elementwise."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "DataFrame.ne",
        "ref": null,
        "exists": null
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compare DataFrames for inequality elementwise."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    }
  ],
  "version": "1.4.0",
  "signature": "f(self, other, axis='columns', level=None)",
  "references": null,
  "logo": "logo.png",
  "qa": "pandas.core.ops.flex_comp_method_FRAME.<locals>.f",
  "arbitrary": []
}