# Builds the 1x preview GIF, a seamless-loop check and 360px background composites from the 2x strip.
from PIL import Image
import numpy as np, json
st=Image.open("fx_stop_marker_neutral_strip@2x.png").convert("RGBA"); N=12
fr=[st.crop((i*96,0,i*96+96,96)) for i in range(N)]
g=[]
for f in fr:
    b=Image.new("RGBA",(48,48),(110,100,130,255)); b.alpha_composite(f.resize((48,48),Image.LANCZOS)); g.append(b.convert("P",palette=Image.ADAPTIVE))
g[0].save("fx_stop_marker_neutral_preview_1x.gif",save_all=True,append_images=g[1:],duration=83,loop=0,disposal=2)
a=[np.asarray(f,dtype=float) for f in fr]; steps=[np.abs(a[(i+1)%N]-a[i]).mean() for i in range(N)]
print("step diffs (last = wrap 11->0):",[round(s,2) for s in steps])
# 360px composites: background 780x1688 -> 360x779; marker 1x=48 css px at 390 -> 44 px at 360; show frames 0 and 6
for bg,pts in (("bg_dog_stop",[(120,330),(250,330)]),("bg_candy_sort",[(120,360),(250,360)])):
    B=Image.open(f"../backgrounds/{bg}.png").convert("RGBA").resize((360,779),Image.LANCZOS)
    s=360/390*48/96
    for (x,y),k in zip(pts,(0,6)):
        m=fr[k].resize((round(96*s),round(96*s)),Image.LANCZOS); B.alpha_composite(m,(x-m.width//2,y-m.height))
    B.save(f"fx_stop_marker_neutral_on_{bg}_360.png")
