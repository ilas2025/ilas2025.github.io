---
title: "LOGO"
type: page
date: 2023-08-05T23:36:06+08:00
---

The conference LOGO is inspired by the
[Great Harbor Bridge](https://khh.travel/en/attractions/detail/1186),
which is a landmark in Kaohsiung featuring its streamlined design.  It
is also the first bridge that can rotate horizontally to let boats
pass through.

If the LOGO is viewed as a graph, then it is the graph with its graph6
string `"G?}WNc"` .  It second smallest Laplacian eigenvalue is
1.6**2025**43669426...

You may run the Sage code below

```python
g = Graph("G?}WNc")
L = g.laplacian_matrix()
g.show()
show(L)
print(sorted(L.eigenvalues()))
```

or use [SageCell](https://sagecell.sagemath.org/?q=kfxpwq) to see the
graph, the Laplacian matrix, and the eigenvalues.
