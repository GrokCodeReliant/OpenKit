# Batch 3: extras galore
cols=[P["pumpkin"],P["teal"],P["berry"],P["candle"],P["plight"],"#7FBF6A","#FFFFFF","#3A3F5C"]
for i,(sc,col) in enumerate(((1,P["pmid"]),(.8,"#3A3F5C"),(1.2,P["plight"]))):
    part(f"x_bat_{i+1}",f'<g transform="scale({sc}) rotate({(-10,6,0)[i]})">'+parts["bat"].replace(P["pmid"],col)+'</g>',"-42 -20 84 40")
for i,(c,pose) in enumerate(((("#3A3F5C"),"sit"),(P["pumpkin"],"walk"),("#FFFFFF","sit"))):
    part(f"x_cat_{i+1}",f'<g transform="scale(1.4)">{kit(pose).replace(P["pumpkin"],c)}</g>',"-38 -38 72 60")
for i in range(3):
    n=5+i; spokes="".join(f'<path d="M0 0 L{40*__import__("math").cos(k*3.14159/2/(n-1)):.1f} {40*__import__("math").sin(k*3.14159/2/(n-1)):.1f}"/>' for k in range(n))
    rings="".join(f'<path d="M{r} 0 Q{r*.8} {r*.8} 0 {r}" fill="none"/>' for r in (14,26,38)[:i+2])
    part(f"x_cobweb_{i+1}",f'<g stroke="{P["ink"]}" stroke-width="2.6" stroke-linecap="round" fill="none">{spokes}{rings}</g><g stroke="{P["cream"]}" stroke-width="1.2" stroke-linecap="round" fill="none">{spokes}{rings}</g>',"-2 -2 44 44")
for i,sh in enumerate(("M-20 30 V-10 q0 -22 20 -22 q20 0 20 22 V30z","M-18 30 V-24 h36 V30z","M-22 30 V-8 q0 -24 22 -24 q22 0 22 24 V30z","M-22 30 V0 q0 -14 10 -14 q4 -12 12 -12 q8 0 12 12 q10 0 10 14 V30z")):
    extra=(f'<path d="M15 -27 l-3 7 l4 4 l-3 7" fill="none" {O(2)}/><path d="M-22 18 q6 -8 12 -2 q4 -6 10 0 v14 h-22z" fill="#7FBF6A" {O(2)}/><circle cx="-14" cy="10" r="3" fill="#9BD06A" {O(1.5)}/>' if i==2 else "")
    part(f"x_gravestone_{i+1}",f'<ellipse cx="0" cy="30" rx="26" ry="6" fill="#7FBF6A" {O(2)}/><path d="{sh}" fill="#B9B4C8" {O()}/><path d="M-6 6 q6 6 12 0" fill="none" {O(2)}/><circle cx="-6" cy="-4" r="2" fill="{P["ink"]}"/><circle cx="6" cy="-4" r="2" fill="{P["ink"]}"/>'+extra,"-28 -36 56 72")
for i,(c,kind) in enumerate(((P["cream"],"picket"),(P["wood"],"rail"),("#3A3F5C","iron"))):
    if kind=="picket": b="".join(f'<path d="M{x} 30 V0 l6 -8 l6 8 V30z" fill="{c}" {O(2)}/>' for x in range(-46,40,18))
    elif kind=="rail": b=f'<g {O()}><rect x="-48" y="-4" width="96" height="10" fill="{c}"/><rect x="-48" y="14" width="96" height="10" fill="{c}"/>'+"".join(f'<rect x="{x}" y="-10" width="10" height="42" fill="{c}"/>' for x in (-44,-5,34))+'</g>'
    else: b=f'<g {O(3)}><path d="M-48 0 H48 M-48 20 H48"/>'+"".join(f'<path d="M{x} 32 V-8"/><circle cx="{x}" cy="-10" r="3" fill="{P["pumpkin"]}"/>' for x in range(-44,48,12))+'</g>'
    part(f"x_fence_{i+1}",b,"-52 -16 104 50")
part("x_moon_crescent",f'<path d="M0 -40 A40 40 0 1 0 0 40 A28 40 0 1 1 0 -40z" fill="#C9F3EC" {O()}/>',"-44 -44 60 88")
part("x_moon_half",f'<path d="M0 -40 a40 40 0 0 0 0 80z" fill="#C9F3EC" {O()}/><circle cx="-16" cy="-6" r="6" fill="#A6E6DC"/>',"-44 -44 48 88")
part("x_moon_smiley",f'<circle r="40" fill="#C9F3EC" {O()}/><circle cx="-12" cy="-6" r="4" fill="{P["ink"]}"/><circle cx="12" cy="-6" r="4" fill="{P["ink"]}"/><path d="M-12 10 q12 12 24 0" fill="none" {O()}/>',"-44 -44 88 88")
candies={"wrapped":lambda c:f'<path d="M-24 -8 l10 8 l-10 8z M24 -8 l-10 8 l10 8z" fill="{c}" {O(2)}/><ellipse rx="14" ry="10" fill="{c}" {O()}/>',
 "lollipop":lambda c:f'<path d="M0 6 v22" stroke="{P["cream"]}" stroke-width="5" stroke-linecap="round"/><circle cy="-6" r="14" fill="{c}" {O()}/><path d="M-6 -6 a6 6 0 1 1 6 6" fill="none" stroke="#FFFFFF" stroke-width="3"/>',
 "corn":lambda c:f'<path d="M-14 12 L0 -18 L14 12z" fill="#FFFFFF" {O()}/><path d="M-14 12 h28 L10 4 h-20z" fill="{P["pumpkin"]}"/><path d="M-6 -4 h12 L0 -18z" fill="{P["candle"]}"/>',
 "bar":lambda c:f'<rect x="-18" y="-10" width="36" height="20" rx="3" fill="{c}" {O()}/><rect x="-8" y="-10" width="16" height="20" fill="{P["cream"]}" {O(2)}/>'}
k=0
for t,f in candies.items():
    for c in ((P["berry"],P["teal"]) if t!="corn" else (None,None)):
        k+=1; part(f"x_candy_{t}_{k}",f(c),"-28 -26 56 56")
part("x_candy_gum_drop",f'<path d="M-14 12 q0 -26 14 -26 q14 0 14 26z" fill="#7FBF6A" {O()}/>',"-20 -18 40 34")
part("x_candy_star",parts["marker_star"].replace(P["candle"],P["berry"]),"-24 -24 48 46")
CP={"x_costume_witch_hat":f'<path d="M-26 6 h52 q-6 -8 -18 -8 L6 -34 l-16 10 L-8 -2 q-12 0 -18 8z" fill="{P["plight"]}" {O()}/><path d="M-8 -2 h16" stroke="{P["candle"]}" stroke-width="4"/>',
 "x_costume_cape":f'<path d="M-14 -20 h28 l12 46 q-26 8 -52 0z" fill="{P["berry"]}" {O()}/>',
 "x_costume_crown":f'<path d="M-18 8 V-10 l9 8 l9 -12 l9 12 l9 -8 V8z" fill="{P["candle"]}" {O()}/>',
 "x_costume_wand":f'<path d="M-16 20 L8 -6" {O(4)}/><path d="M10 -18 l3 7 l7 1 l-5 5 l1 7 l-6 -3 l-6 3 l1 -7 l-5 -5 l7 -1z" fill="{P["candle"]}" {O(2)}/>',
 "x_costume_mask":f'<path d="M-24 -6 q12 -10 24 0 q12 -10 24 0 q0 14 -12 14 q-8 0 -12 -6 q-4 6 -12 6 q-12 0 -12 -14z" fill="{P["teal"]}" {O()}/><ellipse cx="-11" cy="0" rx="5" ry="3" fill="{P["ink"]}"/><ellipse cx="11" cy="0" rx="5" ry="3" fill="{P["ink"]}"/>',
 "x_costume_bow_tie":f'<path d="M0 0 L-18 -10 v20z M0 0 L18 -10 v20z" fill="{P["berry"]}" {O()}/><circle r="5" fill="{P["berry"]}" {O(2)}/>',
 "x_costume_pirate_hat":f'<path d="M-26 6 q26 -40 52 0 q-26 -8 -52 0z" fill="#3A3F5C" {O()}/><circle cy="-8" r="4" fill="{P["cream"]}"/>',
 "x_costume_bunny_ears":f'<ellipse cx="-8" cy="-12" rx="6" ry="16" fill="#FFFFFF" {O()}/><ellipse cx="8" cy="-12" rx="6" ry="16" fill="#FFFFFF" {O()}/><ellipse cx="-8" cy="-12" rx="2.5" ry="10" fill="{P["berry"]}"/><ellipse cx="8" cy="-12" rx="2.5" ry="10" fill="{P["berry"]}"/><rect x="-16" y="4" width="32" height="5" rx="2" fill="{P["plight"]}" {O(2)}/>'}
for n,b in CP.items(): part(n,b,"-30 -36 60 66")
PR={"x_prop_hay_bale":f'<rect x="-28" y="-14" width="56" height="30" rx="5" fill="#E8C07A" {O()}/><path d="M-28 -2 h56 M-14 -14 v30 M14 -14 v30" stroke="{P["pdark"]}" stroke-width="2"/>',
 "x_prop_scarecrow":DEC["deco_scarecrow_mini"],
 "x_prop_lantern":f'<path d="M-8 -20 h16 M0 -26 v6" {O(2)}/><rect x="-12" y="-20" width="24" height="34" rx="4" fill="{P["candle"]}" {O()}/><path d="M-12 -8 h24 M-12 4 h24" {O(2)}/>',
 "x_prop_leaf_pile":"".join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="6" fill="{c}" {O(2)} transform="rotate({r} {x} {y})"/>' for x,y,c,r in ((-14,10,P["pumpkin"],20),(8,12,P["berry"],-15),(0,2,P["candle"],5),(16,4,P["pdark"],30),(-8,-4,"#E08A3C",-25))),
 "x_prop_cauldron":f'<path d="M-24 -6 q0 30 24 30 q24 0 24 -30z" fill="#3A3F5C" {O()}/><ellipse cy="-6" rx="26" ry="7" fill="#9BE07A" {O()}/><circle cx="-6" cy="-12" r="4" fill="#9BE07A" {O(2)}/>',
 "x_prop_broom":f'<path d="M-24 -20 L10 12" stroke="{P["wood"]}" stroke-width="6" stroke-linecap="round"/><path d="M8 6 l18 6 l-4 10 l-10 4z" fill="#E8C07A" {O()}/>',
 "x_prop_candy_sign_post":f'<rect x="-3" y="-6" width="6" height="32" fill="{P["wood"]}" {O(2)}/><rect x="-24" y="-24" width="48" height="20" rx="5" fill="{P["cream"]}" {O()}/>',
 "x_prop_skull_toy":f'<path d="M-12 -20 L-2 -40 L8 -20z" fill="{P["teal"]}" {O(2.5)}/><circle cx="-2" cy="-41" r="3.5" fill="{P["candle"]}" {O(2)}/><circle cy="-4" r="16" fill="#FFFFFF" {O()}/><rect x="-9" y="8" width="18" height="9" rx="4" fill="#FFFFFF" {O()}/><circle cx="-6" cy="-5" r="5" fill="#FFFFFF" {O(2)}/><circle cx="6" cy="-5" r="5" fill="#FFFFFF" {O(2)}/><circle cx="-5" cy="-4" r="2.2" fill="{P["ink"]}"/><circle cx="7" cy="-6" r="2.2" fill="{P["ink"]}"/><path d="M-2 10 q2 9 6 0z" fill="{P["berry"]}" {O(1.5)}/><circle cx="-12" cy="2" r="3" fill="{P["berry"]}" opacity=".5"/><circle cx="12" cy="2" r="3" fill="{P["berry"]}" opacity=".5"/>', "x_prop_balloon_ghost":f'<path d="M0 18 q-4 8 2 16" fill="none" {O(1.5)}/>'+parts["ghost_sheet"].replace('<path d="M-18 18','<path transform="scale(.7)" d="M-18 18'),
 "x_prop_tombstone_cake":f'<path d="M-18 20 V-6 q0 -16 18 -16 q18 0 18 16 V20z" fill="#8C5A3C" {O()}/><path d="M-18 -2 q9 6 18 0 q9 6 18 0" fill="none" stroke="{P["cream"]}" stroke-width="4"/>'}
for n,b in PR.items(): part(n,b,"-32 -32 64 64")

# ---- extra full-screen backgrounds (390x844 masters -> backgrounds/*.png at 780x1688). Middle band y≈250..620 kept clear for UI.
def _clear(y0=250,y1=620,c=None): return f'<rect x="20" y="{y0}" width="350" height="{y1-y0}" rx="26" fill="{c or P["cream"]}" opacity=".16"/>'
def _doghouse(x,y,s=1): return (f'<g transform="translate({x},{y}) scale({s})" {O()}><path d="M-40 0 V-50 L0 -84 L40 -50 V0z" fill="{P["berry"]}"/><path d="M-48 -46 L0 -90 L48 -46" fill="none" stroke-width="8"/>'
    f'<path d="M-48 -46 L0 -90 L48 -46" fill="none" stroke="{P["plight"]}" stroke-width="4"/><path d="M-16 0 V-26 q16 -20 32 0 V0z" fill="{P["ink"]}"/></g>')
part("bg_dog_stop",f'<rect width="390" height="844" fill="{P["grass"]}"/>'
  +f'<g transform="translate(195,236) scale(.9)">{porch(P["house1"],"#C2603F")}</g>'
  +"".join(f'<path d="M{x} 244 V214 l6 -8 l6 8 V244z" fill="{P["cream"]}" {O(2)}/>' for x in list(range(0,60,16))+list(range(322,390,16)))
  +_clear()
  +f'<rect x="-5" y="650" width="400" height="70" fill="{P["walk"]}" {O()}/>'+"".join(f'<path d="M{x} 653 v64" stroke="#B9B1A2" stroke-width="2"/>' for x in range(48,390,48))
  +_doghouse(70,790,1.0)
  +f'<g {O()}><ellipse cx="300" cy="790" rx="30" ry="12" fill="{P["teal"]}"/><ellipse cx="300" cy="786" rx="22" ry="7" fill="#E9C07A"/></g>'
  +f'<g transform="translate(185,780) scale(.9)">{parts["item_dog_treats"]}</g>')
part("bg_costume_fixup",f'<rect width="390" height="844" fill="{P["pmid"]}"/><rect y="700" width="390" height="144" fill="#6B4F8C"/>'
  +"".join(f'<path d="M{x} 700 v144" stroke="{P["purple"]}" stroke-width="2"/>' for x in range(0,390,40))
  +f'<path d="M30 70 H360" {O(5)}/>'
  +"".join(f'<g transform="translate({x},70)"><path d="M0 0 v10 M-14 22 L0 10 L14 22" fill="none" {O(2.5)}/><g transform="translate(0,{dy}) scale(1.6)">{parts[n]}</g></g>' for x,n,dy in ((70,"x_costume_cape",70),(150,"costume_robot_torso",112),(230,"costume_cat_torso",110),(310,"costume_bee_torso",106)))
  +_clear(260,620)
  +f'<g {O()}><rect x="20" y="660" width="350" height="26" rx="6" fill="{P["wood"]}"/><path d="M40 686 v110 M350 686 v110" stroke-width="8"/></g>'
  +f'<g transform="translate(90,646) scale(1.1)">{parts["x_costume_witch_hat"]}</g><g transform="translate(200,650)">{parts["x_costume_crown"]}</g><g transform="translate(300,648)">{parts["x_costume_mask"]}</g>'
  +f'<g transform="translate(330,790) scale(1.2)">{parts["item_tape"].replace("<g","<g transform=\"translate(-20,-20)\"",1)}</g><g transform="translate(80,790)" {O()}><ellipse rx="40" ry="16" fill="{P["berry"]}"/><path d="M-40 0 q40 18 80 0" fill="none" stroke-width="2"/><circle cx="-10" cy="-10" r="8" fill="{P["candle"]}"/><circle cx="10" cy="-12" r="7" fill="{P["teal"]}"/></g>')
part("bg_candy_sort",f'<rect width="390" height="844" fill="{P["purple"]}"/>'
  +f'<g {O()}><rect x="0" y="40" width="390" height="190" fill="{P["house2"]}"/><rect x="0" y="40" width="390" height="14" fill="{shade(P["house2"],.8)}" stroke="none"/><rect x="150" y="80" width="90" height="150" rx="6" fill="{P["wood"]}"/><circle cx="225" cy="160" r="5" fill="{P["candle"]}"/>'
  +f'<rect x="30" y="90" width="80" height="60" rx="4" fill="{P["candle"]}"/><rect x="280" y="90" width="80" height="60" rx="4" fill="{P["candle"]}"/><path d="M70 90 v60 M320 90 v60 M30 120 h80 M280 120 h80" stroke-width="2"/></g>'
  +f'<rect x="-5" y="228" width="400" height="30" fill="#CDBBA2" {O()}/>'
  +f'<g transform="translate(40,200) scale(.8)">{parts["jack_carved"]}</g><g transform="translate(350,204) scale(.7)">{parts["jack_carved_unlit"]}</g>'
  +_clear(270,620)
  +f'<g {O()}><rect x="10" y="650" width="370" height="40" rx="10" fill="{P["wood"]}"/><rect x="10" y="690" width="370" height="154" fill="{shade(P["wood"],.8)}"/></g>'
  +"".join(f'<g transform="translate({x},640)" {O()}><path d="M-44 0 q0 40 44 40 q44 0 44 -40z" fill="{c}"/><ellipse rx="44" ry="10" fill="{shade(c,.8)}"/></g>' for x,c in ((75,P["teal"]),(195,P["berry"]),(315,P["candle"])))
  +"".join(f'<g transform="translate({x},{y}) rotate({r}) scale(.7)">{parts[n]}</g>' for x,y,r,n in ((40,780,20,"x_candy_wrapped_1"),(120,800,-15,"x_candy_lollipop_3"),(270,790,30,"x_candy_corn_5"),(340,810,-20,"x_candy_bar_7"),(195,815,0,"x_candy_star"))))

# ---- extra groceries (bag sprites; 48 px cells, 52 px pitch, 4 px inset)
item("flour",1,2,lambda w,h:g(f'<path d="M{w*.3} {h*.2} C-6 {h*.32} -4 {h-4} {w*.2} {h-3} H{w*.8} C{w+4} {h-4} {w+6} {h*.32} {w*.7} {h*.2}z" fill="#E9C07A"/>'
  f'<path d="M{w*.3} {h*.2} l-6 -{h*.12} l{w*.16} {h*.05} l{w*.04} -{h*.08} l{w*.04} {h*.08} l{w*.16} -{h*.05} l-6 {h*.12}z" fill="#E9C07A"/><path d="M{w*.28} {h*.2} h{w*.44}" stroke="{P["berry"]}" stroke-width="4"/>'
  f'<rect x="{w*.18}" y="{h*.42}" width="{w*.64}" height="{h*.36}" rx="6" fill="{P["cream"]}" stroke-width="2"/>'
  +f'<path d="M{w/2} {h*.74} V{h*.48}" stroke="{P["pdark"]}" stroke-width="2"/>'+"".join(f'<ellipse cx="{w/2+sx*4}" cy="{y}" rx="3.5" ry="2" fill="{P["candle"]}" stroke-width="1.2" transform="rotate({sx*-35} {w/2+sx*4} {y})"/>' for sx in (-1,1) for y in (h*.52,h*.6,h*.68))
  +f'<circle cx="{w*.82}" cy="{h*.08}" r="3" fill="#FFFFFF" stroke-width="1.5"/><circle cx="{w*.92}" cy="{h*.02}" r="2" fill="#FFFFFF" stroke-width="1.5"/>'))
item("eggs",2,1,lambda w,h:g(f'<path d="M4 {h*.42} H{w-4} L{w-10} {h-4} H10z" fill="{P["plight"]}"/>'
  +"".join(f'<ellipse cx="{w*(.2+k*.2)}" cy="{h*.38}" rx="{w*.08}" ry="{h*.24}" fill="#FFFFFF"/>' for k in range(4))
  +f'<path d="M4 {h*.42} H{w-4} L{w-10} {h-4} H10z" fill="{P["plight"]}"/>'+"".join(f'<path d="M{w*(.3+k*.2)} {h*.46} v{h*.4}" stroke="{P["purple"]}" stroke-width="2"/>' for k in range(3))
  +f'<path d="M{w*.8} {h*.16} l-4 6 l6 4 l-4 7" fill="none" stroke-width="2.5"/>'))

# ======== Final pass (2026-10-23): drop-in frames the game looks up (requests.md rows 51, 55, 61-65) ========
import json as _json, os as _os
SKIN,HAIR_A,HAIR_B,BAGC,BAGD="#E8B48A","#3B2A22","#6B3A1E","#C99B62","#A77A45"   # match game/worker.ts
def _bag(x,y,s=1,rot=0): return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})" {O()}><path d="M-6 -12 q6 -9 12 0" fill="none" stroke-width="2.5"/>'
    f'<rect x="-9" y="-12" width="18" height="16" rx="4" fill="{BAGC}"/><path d="M-9 -4 h18" stroke="{BAGD}" stroke-width="2"/></g>')
def _head(x,y,hair,down=0):
    return (f'<g {O()}><circle cx="{x}" cy="{y}" r="11" fill="{SKIN}"/><circle cx="{x-11}" cy="{y+1}" r="3" fill="{SKIN}" stroke-width="2"/><circle cx="{x+11}" cy="{y+1}" r="3" fill="{SKIN}" stroke-width="2"/>'
            f'<path d="M{x-11} {y+2-down} q-1 -15 11 -15 q12 0 11 15 q-5 4 -11 4 q-6 0 -11 -4z" fill="{hair}"/></g>')
def _stand(hair,tilt=0,arm=0,bags=True,shift=0):
    # back view, feet at (0,0). tilt rotates around the feet; arm = arms flung up (0..1)
    ax=10+10*arm; ay=-60-18*arm
    b=(f'<g transform="rotate({tilt})"><g {O()}><rect x="-12" y="-30" width="10" height="28" rx="4" fill="{P["purple"]}"/><rect x="2" y="-30" width="10" height="28" rx="4" fill="{P["purple"]}"/>'
       f'<rect x="-13" y="-6" width="12" height="7" rx="3" fill="{P["night"]}"/><rect x="1" y="-6" width="12" height="7" rx="3" fill="{P["night"]}"/>'
       f'<path d="M-16 -62 h32 l2 34 h-36z" fill="{P["teal"]}"/></g>'
       f'<path d="M-15 -58 L{-ax} {ay+30} M15 -58 L{ax} {ay+30}" stroke="{P["ink"]}" stroke-width="10" stroke-linecap="round"/><path d="M-15 -58 L{-ax} {ay+30} M15 -58 L{ax} {ay+30}" stroke="{P["teal"]}" stroke-width="5" stroke-linecap="round"/>'
       f'<circle cx="{-ax}" cy="{ay+31}" r="4.5" fill="{SKIN}" {O(2.5)}/><circle cx="{ax}" cy="{ay+31}" r="4.5" fill="{SKIN}" {O(2.5)}/>'
       +(_bag(-ax,ay+46)+_bag(ax,ay+46) if bags else "")+_head(0,-74,hair)+'</g>')
    return f'<g transform="translate({shift},0)">{b}</g>'
def _sit(hair,breath=0):
    up=-1.5*breath
    return (""
      +_bag(-26,0)+_bag(27,0,1,8)
      +f'<g {O()}><path d="M-14 -4 q-6 4 -10 4 h-2 v-8 h6 z" fill="{P["night"]}"/><path d="M14 -4 q6 4 10 4 h2 v-8 h-6z" fill="{P["night"]}"/>'
      f'<rect x="-14" y="-14" width="28" height="12" rx="6" fill="{P["purple"]}"/>'
      f'<path d="M-16 {-44+up} h32 l2 32 h-36z" fill="{P["teal"]}"/></g>'
      f'<path d="M-15 {-40+up} q-6 14 -2 26 M15 {-40+up} q6 14 2 26" fill="none" stroke="{P["ink"]}" stroke-width="10" stroke-linecap="round"/><path d="M-15 {-40+up} q-6 14 -2 26 M15 {-40+up} q6 14 2 26" fill="none" stroke="{P["teal"]}" stroke-width="5" stroke-linecap="round"/>'
      f'<circle cx="-17" cy="-13" r="4.5" fill="{SKIN}" {O(2.5)}/><circle cx="17" cy="-13" r="4.5" fill="{SKIN}" {O(2.5)}/>'
      +_head(0,-55+up,hair,down=1)
      +(f'<g opacity=".85"><circle cx="16" cy="-70" r="4" fill="{P["cream"]}" {O(1.5)}/><circle cx="23" cy="-76" r="2.6" fill="{P["cream"]}" {O(1.5)}/></g>' if breath else ""))
def _kneel(hair):
    return (""+_bag(-24,0)+_bag(25,0)
      +f'<g {O()}><rect x="-12" y="-22" width="10" height="20" rx="4" fill="{P["purple"]}"/><path d="M2 -26 h10 v16 h8 v8 h-18z" fill="{P["purple"]}"/>'
      f'<path d="M-16 -54 h32 l2 32 h-36z" fill="{P["teal"]}"/></g>'
      f'<path d="M-15 -50 L-22 -26 M15 -50 L22 -26" stroke="{P["ink"]}" stroke-width="10" stroke-linecap="round"/><path d="M-15 -50 L-22 -26 M15 -50 L22 -26" stroke="{P["teal"]}" stroke-width="5" stroke-linecap="round"/>'
      f'<circle cx="-22" cy="-24" r="4.5" fill="{SKIN}" {O(2.5)}/><circle cx="22" cy="-24" r="4.5" fill="{SKIN}" {O(2.5)}/>'+_head(0,-66,hair))
def _shadow(rx=24): return ""  # no shading per style rules
SEQ=lambda hair:[("fall",_shadow()+_stand(hair,12,.2)),("fall",_shadow()+_stand(hair,38,.7,shift=-16)),("fall",_shadow(30)+_stand(hair,68,1,bags=False,shift=-38)+_bag(-30,0,1,-30)+_bag(34,-2,1,40)),
  ("sit",_sit(hair,0)),("sit",_sit(hair,1)),("getup",_kneel(hair)),("getup",_shadow()+_stand(hair,-6,0))]
for wk,hair in (("A",HAIR_A),("B",HAIR_B)):
    seq=SEQ(hair)
    # single atlas frames (row 64): 60x90 at 1x, feet at bottom-centre
    part(f"wk{wk}_fall",f'<g transform="translate(30,88) scale(.62)">{seq[2][1]}</g>',"0 0 60 90")
    part(f"wk{wk}_sit",f'<g transform="translate(30,88)">{seq[3][1]}</g>',"0 0 60 90")
    part(f"wk{wk}_sit_1",f'<g transform="translate(30,88)">{seq[4][1]}</g>',"0 0 60 90")
    # strip (like fx_stop_marker): 96x96 at 1x per frame, 2x render, anchor (0.5,1.0)
    FD=_os.path.join(_os.path.dirname(_os.path.abspath("build.py")),"../fx"); _os.makedirs(FD,exist_ok=True)
    order=[0,1,2,3,4,3,4,5,6]; N=len(order)
    cells="".join(f'<svg x="{i*192}" y="0" width="192" height="192" viewBox="0 0 96 96"><g transform="translate(48,93)">{seq[k][1]}</g></svg>' for i,k in enumerate(order))
    open(f"{FD}/wk{wk}_fall_strip@2x.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{192*N}" height="192">{cells}</svg>')
    _json.dump(dict(name=f"wk{wk}_fall",image=f"wk{wk}_fall_strip@2x.png",scale=2,frame_size=dict(w=192,h=192),size_1x=dict(w=96,h=96),
      frames=[dict(i=i,x=i*192,y=0,w=192,h=192,pose=seq[k][0]) for i,k in enumerate(order)],fps=6,segment_fps=dict(fall=6,sit_loop=2,getup=4),
      segments=dict(fall=[0,1,2],sit_loop=[3,4,5,6],getup=[7,8]),loop_segment="sit_loop",anchor=dict(x=0.5,y=1.0),
      notes="Feet/seat point = anchor (same as drawWorker's x,y between the feet). Play fall once, loop sit_loop for the rest (REST_SEC), then getup once. Rig scale ~1x (figure ~88 px tall standing). Teal uniform; orange option via tint not included.",
      license="CC0, original crew work"),open(f"{FD}/wk{wk}_fall.json","w"),indent=1)
# store icons (row 65): 48x48 like item_*
item("compass",1,1,lambda w,h:g(f'<circle cx="{w/2}" cy="5" r="4" fill="none" stroke-width="2.5"/><circle cx="{w/2}" cy="{h/2+3}" r="{w*.4}" fill="{P["candle"]}"/><circle cx="{w/2}" cy="{h/2+3}" r="{w*.29}" fill="{P["cream"]}" stroke-width="2"/>'
  f'<path d="M{w/2} {h/2+3-w*.24} l4 {w*.24} h-8z" fill="{P["berry"]}" stroke-width="1.5"/><path d="M{w/2} {h/2+3+w*.24} l4 -{w*.24} h-8z" fill="{P["tdark"]}" stroke-width="1.5"/><circle cx="{w/2}" cy="{h/2+3}" r="2" fill="{P["ink"]}"/>'))
item("duster",1,1,lambda w,h:g(f'<path d="M{w*.2} {h-4} L{w*.55} {h*.48}" stroke="{P["wood"]}" stroke-width="5"/><path d="M{w*.2} {h-4} L{w*.55} {h*.48}" fill="none" stroke-width="1.5"/>'
  +"".join(f'<ellipse cx="{w*.62+dx}" cy="{h*.32+dy}" rx="8" ry="11" fill="{c}" transform="rotate({r} {w*.62+dx} {h*.32+dy})"/>' for dx,dy,r,c in ((-6,4,-40,P["plight"]),(6,4,40,P["plight"]),(0,-4,0,P["cream"])))
  +f'<path d="M{w*.82} {h*.12} q6 6 2 14" fill="none" stroke="{P["cream"]}" stroke-width="1.2"/>'))
# landmarks (rows 62, 63)
part("lm_dead_tree",g(f'<path d="M28 70 q2 -18 0 -36 q-8 -10 -18 -14 l2 -4 q10 2 16 10 q0 -10 -6 -20 l4 -2 q6 8 6 18 q6 -10 16 -12 l1 4 q-10 4 -14 14 q0 16 2 42z" fill="{P["wood"]}"/><path d="M30 46 l4 -4 M26 30 l-3 -2" fill="none" stroke-width="2"/>'),"0 -2 64 74")
part("lm_gnome",g(f'<path d="M8 58 q0 -24 11 -24 q11 0 11 24z" fill="{P["tdark"]}"/><path d="M8 26 h22 L21 2 z" fill="{P["berry"]}"/><circle cx="19" cy="30" r="7" fill="{SKIN}"/>'
  f'<path d="M11 31 q8 22 16 0 q-8 3 -16 0z" fill="{P["cream"]}"/><circle cx="19" cy="32" r="3" fill="{P["berry"]}" stroke-width="2"/><rect x="9" y="56" width="9" height="5" rx="2" fill="{P["ink"]}"/><rect x="20" y="56" width="9" height="5" rx="2" fill="{P["ink"]}"/>'),"0 -1 38 63")
# "Home ->" fingerpost (row 61): blank board, anchor bottom-centre of the post
part("walk_sign_home",g(f'<rect x="25" y="16" width="6" height="44" fill="{P["wood"]}"/><rect x="4" y="6" width="48" height="22" rx="5" fill="#F2E2C4"/>'),"0 3 56 60")
# porch cues (row 55): about 64x64, transparent
part("porch_cue_hook",f'<circle cx="32" cy="32" r="26" fill="{P["candle"]}" opacity=".18"/>'+g(f'<circle cx="32" cy="18" r="4" fill="{P["plight"]}"/><path d="M32 22 v14 q0 10 -8 10 q-6 0 -6 -6" fill="none" stroke-width="6"/><path d="M32 22 v14 q0 10 -8 10 q-6 0 -6 -6" fill="none" stroke="{P["candle"]}" stroke-width="3"/>'),"0 0 64 64")
part("porch_cue_cobweb",f'<g transform="translate(6,6) scale(1.2)">{parts["x_cobweb_2"]}</g>',"0 0 64 64")
part("porch_cue_step",f'<ellipse cx="32" cy="34" rx="28" ry="16" fill="{P["candle"]}" opacity=".18"/>'+g(f'<path d="M8 44 h48 l-6 -14 h-36z" fill="{P["pmid"]}"/><path d="M8 44 h48 v8 h-48z" fill="{P["purple"]}"/>'),"0 0 64 64")
# route props on transparent (row 51): anchor bottom-centre
part("route_mailbox",g(f'<rect x="7" y="18" width="4" height="20" fill="{P["wood"]}" stroke-width="2"/><path d="M2 20 V9 q0 -7 7 -7 q7 0 7 7 V20z" fill="{P["berry"]}" stroke-width="2.5"/><path d="M13 7 v-6 h4 v3 h-4" fill="{P["candle"]}" stroke-width="1.5"/>'),"0 0 18 38")
part("route_streetlight",g(f'<rect x="12" y="20" width="6" height="88" fill="{P["plight"]}" stroke-width="2.5"/><path d="M15 22 q0 -12 10 -12" fill="none" stroke-width="3"/><path d="M18 4 h10 l2 8 h-14z" fill="{P["pmid"]}" stroke-width="2.5"/><ellipse cx="15" cy="108" rx="8" ry="2.5" fill="{P["pmid"]}" stroke-width="2"/>')+f'<ellipse cx="23" cy="13" rx="5" ry="2" fill="{P["candle"]}"/>',"0 0 30 110")
part("route_hedge",f'<rect x="1.5" y="0" width="21" height="72" fill="{P["grass2"]}"/><rect x="5" y="0" width="5" height="72" fill="#8FCB7A" opacity=".6"/><path d="M1.5 0 V72 M22.5 0 V72" stroke="{P["ink"]}" stroke-width="3"/>'+"".join(f'<path d="M{x} {y} l3 -4 l3 4" fill="none" stroke="#4E8E46" stroke-width="2" stroke-linecap="round"/>' for x,y in ((6,14),(12,30),(7,48),(13,62))),"0 0 24 72")
part("route_fence",f'<rect x="6" y="0" width="4" height="72" fill="#F4EBDD"/><path d="M6 0 V72 M10 0 V72" stroke="{P["ink"]}" stroke-width="2"/>'+"".join(f'<rect x="1.5" y="{y}" width="13" height="7" rx="2.5" fill="#F4EBDD" stroke="{P["ink"]}" stroke-width="2"/>' for y in (4,16,28,40,52,64)),"0 0 16 72")
# seamless tiles (row 51): no outline at the wrap edges
part("route_lawn_seamless",f'<rect width="128" height="128" fill="{P["grass"]}"/>'+"".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.6}" fill="{P["grass2"]}" opacity=".5"/>' for x,y,r in ((30,40,14),(96,90,16),(80,24,8),(24,104,9)))
  +"".join(f'<path d="M{x} {y} l3 -6 l3 6" fill="none" stroke="#5E9E52" stroke-width="2" stroke-linecap="round"/>' for x,y in ((18,22),(60,58),(104,40),(44,96),(88,112),(112,74))),"0 0 128 128")
part("route_sidewalk_seamless",f'<rect width="150" height="72" fill="{P["walk"]}"/><rect x="0" y="0" width="6" height="72" fill="#A89E8C"/><rect x="144" y="0" width="6" height="72" fill="#A89E8C"/><path d="M6 0 V72 M144 0 V72" stroke="{P["ink"]}" stroke-width="2"/>'
  +f'<path d="M6 36 H144" stroke="#B9B1A2" stroke-width="2"/><path d="M75 6 V30 M75 42 V66" stroke="#C9C1B2" stroke-width="1.5"/><circle cx="40" cy="20" r="1.5" fill="#B9B1A2"/><circle cx="110" cy="54" r="1.5" fill="#B9B1A2"/>',"0 0 150 72")

# bag 9-slice (row 41, re-spec 2 cols x 3 rows): body 112 wide = 6+48+4+48+6; anchor top-left
def _bagside(h,top=False,bot=False):
    L=f'<rect x="1.5" y="{0 if not top else 10}" width="109" height="{h-(10 if top else 0)-(1.5 if bot else 0)}" fill="{P["purple"]}"/>'
    e=f'<path d="M1.5 {10 if top else 0} V{h-(1.5 if bot else 0)} M110.5 {10 if top else 0} V{h-(1.5 if bot else 0)}" stroke="{P["ink"]}" stroke-width="3"/><path d="M5 {12 if top else 0} V{h-(5 if bot else 0)} M107 {12 if top else 0} V{h-(5 if bot else 0)}" stroke="{P["plight"]}" stroke-width="2"/>'
    return L+e
for sd in "LR":
    f=-1 if sd=="R" else 1
    hand=f'<path d="M30 12 q0 -10 10 -10 h32 q10 0 10 10" fill="none" stroke="{P["ink"]}" stroke-width="9"/><path d="M30 12 q0 -10 10 -10 h32 q10 0 10 10" fill="none" stroke="{P["pmid"]}" stroke-width="4"/>'
    rim=f'<rect x="1.5" y="10" width="109" height="10" rx="3" fill="{P["pmid"]}" stroke="{P["ink"]}" stroke-width="3"/>'
    part(f"bag_{sd}_top",hand+_bagside(40,top=True)+rim+(f'<circle cx="{14 if sd=="L" else 98}" cy="15" r="2.5" fill="{P["candle"]}"/>'),"0 0 112 40")
    part(f"bag_{sd}_row",_bagside(52),"0 0 112 52")
    part(f"bag_{sd}_bottom",f'<path d="M1.5 0 V16 q0 6.5 6 6.5 h97 q6 0 6 -6.5 V0z" fill="{P["purple"]}" stroke="{P["ink"]}" stroke-width="3"/><path d="M1.5 0 h109" stroke="{P["purple"]}" stroke-width="4"/><path d="M5 0 V14 q0 4 4 4 h94 q4 0 4 -4 V0" fill="none" stroke="{P["plight"]}" stroke-width="2"/>',"0 0 112 24")
