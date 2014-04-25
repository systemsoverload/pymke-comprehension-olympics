"""Diff the code.
Given a list of lines of code for different programmers, generate a diff from
an original program.
"""
og_code = [
    "function iter (a, i)",
    "  i = i + 1",
    "  local v = a[i]",
    "  if v then",
    "    return i, v",
    "  end",
    "end",
]

changes = {
    "jeff": [
        "function iter (obj, iter)",
        "  iter = iter + 1",
        "  local v = obj[iter]",
        "  if v then",
        "    return iter, v",
        "  end",
        "end",
    ],
    "tim": [
        "function itrtr(a, i)",
        "  i = i + 1",
        "  local v = a[i]",
        "  if v then",
        "    return i, v",
        "  end",
        "end",
    ],
    "tom": [
        "function iter(a, i)",
        "    i = i + 1",
        "    local v = a[i]",
        "    if v then",
        "        return i, v",
        "    end",
        "end",
    ],
    "bwayne": [
        "function iter (a, i)",
        "  i = i + 1",
        "  local v = a[i]",
        "  if v then",
        "    return i, v",
        "  end",
        "end",
    ]
}

output = []
expected = ["tim's changes are:\n-function itrtr(a, i)\n+function iter (a, i)\n", "bwayne's changes are:\n", "jeff's changes are:\n-function iter (obj, iter)\n+function iter (a, i)\n-  iter = iter + 1\n+  i = i + 1\n-  local v = obj[iter]\n+  local v = a[i]\n-    return iter, v\n+    return i, v\n", "tom's changes are:\n-function iter(a, i)\n+function iter (a, i)\n-    i = i + 1\n+  i = i + 1\n-    local v = a[i]\n+  local v = a[i]\n-    if v then\n+  if v then\n-        return i, v\n+    return i, v\n-    end\n+  end\n"]


assert(set(output) == set(expected))
