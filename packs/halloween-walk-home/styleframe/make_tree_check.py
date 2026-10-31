# 390px night check for tile_tree / tile_hedge / route_tree with a ~60% dark-blue multiply tint.
def emb(n,x,y,w,h):
    t=open(f"parts/{n}.svg").read(); vb=t.split('viewBox="')[1].split('"')[0]; b=t.split('>',1)[1].rsplit('</svg>',1)[0]
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{vb}">{b}</svg>'
g=['<rect width="390" height="300" fill="#7FBF6A"/>']
for i,t in enumerate(["tile_tree","tile_hedge","tile_lawn","tile_tree"]): g.append(emb(t,i*98-4,10,104,104))
for i,t in enumerate(["tile_hedge","tile_fence","tile_tree","tile_hedge"]): g.append(emb(t,i*98-4,110,104,104))
for x in (40,150,260,350): g.append(emb("route_tree",x-30,210,60,73))
g.append('<rect width="390" height="300" fill="#1B2A6B" opacity=".6" style="mix-blend-mode:multiply"/>')
open("../checks/trees_night_check_390.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="390" height="300">{"".join(g)}</svg>')
