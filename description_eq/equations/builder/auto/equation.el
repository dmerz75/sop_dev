(TeX-add-style-hook
 "equation"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "amsmath"
    "color"
    "graphicx"
    "pdflscape"
    "rotating")))

