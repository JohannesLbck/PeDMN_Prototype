
d1A = [('a1', 'v1'), ('a2', 'v2')]
d1 = ( 'A', 'e1', 'POST', d1A, '', 'v1 = result', '', '')
d2A = [('a1', 'v1'), ('a2', 'v2')]
d2 = ( 'B', 'e1', 'UPDATE', d2A, '', 'v1 = result', '', '')
d3A = [('a1', 'v1'), ('a2', 'v2')]
d3 = ( 'C', 'e1', 'PATCH', d3A, '', 'v1 = result', '', '')
d4A = []
d4 = ( 'D', 'e1', 'GET', d4A, '', 'v1 = result', '', '')
d5A = []
d5 = ( 'E', 'e1', 'GET', d5A, '', 'v1 = result', '', '')

c1 = ()
c2 = ()
c3 = ()
c4 = ()
c5 = ()



I = [hash((d1, c1)), hash((d2,c2)), hash((d3, c3)), hash((d4,c4)), hash((d5, c5))
D = [d1, d2, d3, d4, d5]
C = [c1, c2, c3, c4, c5]

