#!/usr/bin/env python3
"""Gera ícones SVG/PNG para o PWA da Galeria."""
import os

sizes = [72, 96, 128, 192, 512]
os.makedirs('icons', exist_ok=True)

# SVG base — câmera estilizada sobre fundo preto
svg_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{s}" height="{s}">
  <rect width="{s}" height="{s}" rx="{r}" fill="#1c1c1e"/>
  <rect x="{p}" y="{p}" width="{i}" height="{i}" rx="{ir}" fill="#2c2c2e"/>
  <!-- Camera body -->
  <rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="{cr}" fill="#0a84ff"/>
  <!-- Lens -->
  <circle cx="{lx}" cy="{ly}" r="{lr}" fill="#000" opacity="0.5"/>
  <circle cx="{lx}" cy="{ly}" r="{lr2}" fill="#0a84ff" opacity="0.8"/>
  <circle cx="{lx}" cy="{ly}" r="{lr3}" fill="#fff" opacity="0.9"/>
  <!-- Flash bump -->
  <rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="{fr}" fill="#0a84ff"/>
</svg>'''

for s in sizes:
    p = int(s * 0.1)
    i = s - p * 2
    ir = int(s * 0.12)
    r = int(s * 0.22)
    # Camera dimensions
    cw = int(s * 0.62)
    ch = int(s * 0.42)
    cx = (s - cw) // 2
    cy = (s - ch) // 2 + int(s * 0.05)
    cr = int(s * 0.08)
    # Lens
    lx = s // 2
    ly = cy + ch // 2
    lr = int(s * 0.14)
    lr2 = int(s * 0.09)
    lr3 = int(s * 0.04)
    # Flash
    fw = int(s * 0.14)
    fh = int(s * 0.07)
    fx = cx + int(s * 0.06)
    fy = cy - fh // 2
    fr = int(s * 0.03)

    svg = svg_template.format(
        s=s, r=r, p=p, i=i, ir=ir,
        cx=cx, cy=cy, cw=cw, ch=ch, cr=cr,
        lx=lx, ly=ly, lr=lr, lr2=lr2, lr3=lr3,
        fx=fx, fy=fy, fw=fw, fh=fh, fr=fr,
    )
    with open(f'icons/icon-{s}.svg', 'w') as f:
        f.write(svg)

    # Also write as .png placeholder (SVG renamed)
    # Real PNG would need Pillow/cairosvg - provide SVG fallback
    with open(f'icons/icon-{s}.png', 'wb') as f:
        # Write minimal PNG (1x1 transparent) as placeholder
        # In production, use a real PNG generator
        f.write(svg.encode())

print("Icons generated in icons/")
