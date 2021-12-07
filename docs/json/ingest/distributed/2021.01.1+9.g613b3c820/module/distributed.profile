{
  "_content": {
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "This module contains utility functions to construct and manipulate counting data structures for frames."
                }
              }
            ],
            "inner": []
          }
        }
      ],
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
                  "value": "When performing statistical profiling we obtain many call stacks.  We aggregate these call stacks into data structures that maintain counts of how many times each function in that call stack has been called.  Because these stacks will overlap this aggregation counting structure forms a tree, such as is commonly visualized by profiling tools."
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
                  "value": "We represent this tree as a nested dictionary with the following form:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "DefList",
          "data": {
            "children": [
              {
                "lines": {
                  "_lines": [
                    {
                      "_line": "    {",
                      "_number": 8,
                      "_offset": 4
                    }
                  ]
                },
                "wh": {
                  "_lines": []
                },
                "ind": {
                  "_lines": [
                    {
                      "_line": "     'identifier': 'root',",
                      "_number": 9,
                      "_offset": 5
                    },
                    {
                      "_line": "     'description': 'A long description of the line of code being run.',",
                      "_number": 10,
                      "_offset": 5
                    },
                    {
                      "_line": "     'count': 10  # the number of times we have seen this line",
                      "_number": 11,
                      "_offset": 5
                    },
                    {
                      "_line": "     'children': {  # callers of this line. Recursive dicts",
                      "_number": 12,
                      "_offset": 5
                    },
                    {
                      "_line": "         'ident-b': {'description': ...",
                      "_number": 13,
                      "_offset": 5
                    },
                    {
                      "_line": "                   'identifier': 'ident-a',",
                      "_number": 14,
                      "_offset": 5
                    },
                    {
                      "_line": "                   'count': ...",
                      "_number": 15,
                      "_offset": 5
                    },
                    {
                      "_line": "                   'children': {...}},",
                      "_number": 16,
                      "_offset": 5
                    },
                    {
                      "_line": "         'ident-b': {'description': ...",
                      "_number": 17,
                      "_offset": 5
                    },
                    {
                      "_line": "                   'identifier': 'ident-b',",
                      "_number": 18,
                      "_offset": 5
                    },
                    {
                      "_line": "                   'count': ...",
                      "_number": 19,
                      "_offset": 5
                    },
                    {
                      "_line": "                   'children': {...}}}",
                      "_number": 20,
                      "_offset": 5
                    }
                  ]
                },
                "dt": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "{"
                      }
                    }
                  ],
                  "inner": []
                },
                "dd": [
                  {
                    "type": "Paragraph",
                    "data": {
                      "inline": [
                        {
                          "type": "Words",
                          "data": {
                            "value": "'identifier': 'root', 'description': 'A long description of the line of code being run.', 'count': 10  # the number of times we have seen this line 'children': {  # callers of this line. Recursive dicts     'ident-b': {'description': ...               'identifier': 'ident-a',               'count': ...               'children': {...}},     'ident-b': {'description': ...               'identifier': 'ident-b',               'count': ...               'children': {...}}}"
                          }
                        }
                      ],
                      "inner": []
                    }
                  }
                ]
              }
            ]
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "    }"
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Parameters": {
      "children": [],
      "title": null
    },
    "Returns": {
      "children": [],
      "title": null
    },
    "Yields": {
      "children": [],
      "title": null
    },
    "Receives": {
      "children": [],
      "title": null
    },
    "Raises": {
      "children": [],
      "title": null
    },
    "Warns": {
      "children": [],
      "title": null
    },
    "Other Parameters": {
      "children": [],
      "title": null
    },
    "Attributes": {
      "children": [],
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
    "Warnings": {
      "children": [],
      "title": null
    }
  },
  "refs": [],
  "ordered_sections": [
    "Summary",
    "Extended Summary"
  ],
  "item_file": "/Users/bussonniermatthias/dev/distributed/distributed/profile.py",
  "item_line": 0,
  "item_type": "<class 'module'>",
  "aliases": [
    "distributed.profile"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "2021.01.1+9.g613b3c820",
  "signature": null,
  "references": null,
  "logo": "logo.png",
  "qa": "distributed.profile",
  "arbitrary": [
    {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "This module contains utility functions to construct and manipulate counting data structures for frames. "
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
                  "value": "When performing statistical profiling we obtain many call stacks. We aggregate these call stacks into data structures that maintain counts of how many times each function in that call stack has been called. Because these stacks will overlap this aggregation counting structure forms a tree, such as is commonly visualized by profiling tools. "
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
                  "value": "We represent this tree as a nested dictionary with the following form : "
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    }
  ]
}