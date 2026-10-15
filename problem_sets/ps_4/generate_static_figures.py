from pathlib import Path

OUT = Path(__file__).resolve().parent


def esc(s):
    return (str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))


def svg_begin(w, h):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
            '<style>text{font-family:serif;font-size:18px} .small{font-size:15px} .wire{stroke:#000;stroke-width:2;fill:none} .dash{stroke:#777;stroke-width:1;stroke-dasharray:6 6} .box{stroke:#000;stroke-width:2;fill:white}</style>']


def save(name, parts):
    parts.append('</svg>')
    (OUT/name).write_text('\n'.join(parts), encoding='utf-8')


def waveform(parts, label, y, bits, x0=110, step=55, high=0, low=28):
    parts.append(f'<text x="12" y="{y+20}">{esc(label)}</text>')
    pts=[]
    current = bits[0]
    yy = y + (high if current=='1' else low)
    pts.append((x0,yy))
    for i,b in enumerate(bits):
        x1=x0+i*step
        x2=x0+(i+1)*step
        yy = y + (high if b=='1' else low)
        if i==0:
            pts[0]=(x1,yy)
        else:
            prev=bits[i-1]
            prevy=y+(high if prev=='1' else low)
            if prev != b:
                pts.append((x1,prevy)); pts.append((x1,yy))
        pts.append((x2,yy))
    d=' '.join((('M' if j==0 else 'L')+f'{x},{yy}') for j,(x,yy) in enumerate(pts))
    parts.append(f'<path class="wire" d="{d}"/>')


def fig_672():
    w,h=620,360
    p=svg_begin(w,h)
    x0,step=110,55
    for i in range(9):
        x=x0+i*step
        p.append(f'<line class="dash" x1="{x}" y1="18" x2="{x}" y2="330"/>')
    patterns={
        'A₁':'11000111',
        'A₂':'01101110',
        'B₁':'11000011',
        'B₂':'01010101',
        'Cᵢₙ':'00001111'
    }
    for k,(lab,bits) in enumerate(patterns.items()):
        waveform(p,lab,35+k*58,bits,x0,step)
    save('fig_6_72.svg',p)


def fig_674():
    w,h=880,520
    p=svg_begin(w,h)
    x0,step=115,60
    for i in range(6):
        x=x0+i*step
        p.append(f'<line class="dash" x1="{x}" y1="18" x2="{x}" y2="490"/>')
    pats=[('A₀','11001'),('A₁','01100'),('A₂','01111'),('A₃','11110'),
          ('B₀','01010'),('B₁','01110'),('B₂','11001'),('B₃','01001')]
    for k,(lab,bits) in enumerate(pats):
        waveform(p,lab,30+k*55,bits,x0,step)
    # comparator block
    bx,by,bw,bh=500,75,240,345
    p.append(f'<rect class="box" x="{bx}" y="{by}" width="{bw}" height="{bh}"/>')
    p.append(f'<text x="{bx+78}" y="{by+28}">COMP</text>')
    for i in range(4):
        yy=by+68+i*38
        p.append(f'<text class="small" x="{bx-42}" y="{yy+5}">A{i}</text>')
        p.append(f'<line class="wire" x1="{bx-15}" y1="{yy}" x2="{bx}" y2="{yy}"/>')
    p.append(f'<text x="{bx+78}" y="{by+120}">A</text>')
    for i in range(4):
        yy=by+225+i*38
        p.append(f'<text class="small" x="{bx-42}" y="{yy+5}">B{i}</text>')
        p.append(f'<line class="wire" x1="{bx-15}" y1="{yy}" x2="{bx}" y2="{yy}"/>')
    p.append(f'<text x="{bx+78}" y="{by+285}">B</text>')
    outs=[('A > B',by+135),('A = B',by+175),('A < B',by+215)]
    for lab,yy in outs:
        p.append(f'<text x="{bx+95}" y="{yy+5}">{esc(lab)}</text>')
        p.append(f'<line class="wire" x1="{bx+bw}" y1="{yy}" x2="{bx+bw+85}" y2="{yy}"/>')
    save('fig_6_74.svg',p)


def fig_669():
    w,h=760,300
    p=svg_begin(w,h)
    # three full-adder blocks, MSB on left
    xs=[95,300,505]
    vals=[('1','1','Σ₃'),('1','0','Σ₂'),('1','1','Σ₁')]
    for idx,x in enumerate(xs):
        y=90; bw=130; bh=105
        p.append(f'<rect class="box" x="{x}" y="{y}" width="{bw}" height="{bh}"/>')
        p.append(f'<text class="small" x="{x+20}" y="{y+25}">A</text>')
        p.append(f'<text class="small" x="{x+58}" y="{y+25}">B</text>')
        p.append(f'<text class="small" x="{x+92}" y="{y+25}">Cᵢₙ</text>')
        p.append(f'<text class="small" x="{x+14}" y="{y+90}">Cₒᵤₜ</text>')
        p.append(f'<text class="small" x="{x+98}" y="{y+90}">Σ</text>')
        a,b,s=vals[idx]
        ax=x+28; bxp=x+66
        p.append(f'<line class="wire" x1="{ax}" y1="20" x2="{ax}" y2="{y}"/>')
        p.append(f'<line class="wire" x1="{bxp}" y1="20" x2="{bxp}" y2="{y}"/>')
        p.append(f'<text x="{ax-5}" y="16">{a}</text>')
        p.append(f'<text x="{bxp-5}" y="16">{b}</text>')
        # sum output
        sx=x+105
        p.append(f'<line class="wire" x1="{sx}" y1="{y+bh}" x2="{sx}" y2="255"/>')
        p.append(f'<text x="{sx-14}" y="280">{s}</text>')
    # carry chain from right to left
    # right Cin grounded = 0
    rx=xs[2]+105
    p.append(f'<line class="wire" x1="{rx}" y1="90" x2="{rx}" y2="58"/>')
    p.append(f'<line class="wire" x1="{rx}" y1="58" x2="{rx+48}" y2="58"/>')
    p.append(f'<text x="{rx+55}" y="64">0</text>')
    # carry connections: Cout left-lower to next Cin top-right
    for left_i,right_i in [(1,2),(0,1)]:
        xr=xs[right_i]+18; yr=90+82
        xl=xs[left_i]+105; yt=90
        mid=(xs[right_i]+xs[left_i]+130)/2
        p.append(f'<path class="wire" d="M{xr},{yr} L{xr},{235} L{mid},{235} L{mid},{55} L{xl},{55} L{xl},{yt}"/>')
    # MS carry output
    cx=xs[0]+18
    p.append(f'<line class="wire" x1="{cx}" y1="{90+105}" x2="{cx}" y2="255"/>')
    p.append(f'<text x="{cx-14}" y="280">Σ₄</text>')
    save('fig_6_69.svg',p)


def fig_679():
    w,h=580,360
    p=svg_begin(w,h)
    bx,by,bw,bh=240,55,190,245
    p.append(f'<rect class="box" x="{bx}" y="{by}" width="{bw}" height="{bh}"/>')
    p.append(f'<text x="{bx+70}" y="{by+28}">MUX</text>')
    # selects and data inputs
    labels=[('S₀',by+65),('S₁',by+98),('D₀',by+138),('D₁',by+168),('D₂',by+198),('D₃',by+228)]
    for lab,yy in labels:
        p.append(f'<text x="55" y="{yy+5}">{lab}</text>')
        p.append(f'<line class="wire" x1="95" y1="{yy}" x2="{bx}" y2="{yy}"/>')
    for i,yy in enumerate([by+138,by+168,by+198,by+228]):
        p.append(f'<text class="small" x="{bx+18}" y="{yy+5}">{i}</text>')
    # output
    yy=by+145
    p.append(f'<line class="wire" x1="{bx+bw}" y1="{yy}" x2="{bx+bw+95}" y2="{yy}"/>')
    p.append(f'<text x="{bx+bw+108}" y="{yy+6}">Y</text>')
    save('fig_6_79.svg',p)


if __name__ == '__main__':
    fig_669(); fig_672(); fig_674(); fig_679()
    print('Generated static SVG figures.')
