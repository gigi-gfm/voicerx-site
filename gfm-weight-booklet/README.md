# Healthy Weight Booklet — Garcia Family Medicine

A 10-page, print-ready weight-management booklet built around a **100g-carb-
or-less-per-day** week of **Venezuelan dishes** (comida criolla — perico,
carne mechada, pabellón ligero, reina pepiada, pescado, sancocho), with blank
weekly food and exercise logs.

## Pages
1. Cover — *Healthy Weight, One Week at a Time*
2. Start here — the lower-carb approach + safety note
3. Build your plate (½ veg · ¼ protein · ¼ smart carbs)
4. 7-day Venezuelan menu, Days 1–4 (with approx. carb counts)
5. 7-day Venezuelan menu, Days 5–7 + grocery shortlist (lista de mercado)
6. Carb counts at a glance — Venezuelan staples (arepa, caraotas, tajadas…)
7. **Weekly food log** (blank, fillable)
8. **Weekly exercise log** (blank, fillable)
9. A week of easy movement (plan + tips)
10. Back cover — next steps, GFM contact, disclaimer

Every menu day totals **≤ ~98g carbs**; counts are labeled approximate.

## View / print
Open `index.html` in a browser → **Print / Save PDF** (A4, portrait, margins
None, **Background graphics ON**) → exactly 10 pages. A pre-rendered
`GFM-Healthy-Weight-Booklet.pdf` is included.

## Photos
Pages 1, 2, 3, 6, and 9 use **licensed Adobe Stock photos** (free collection,
royalty-free Standard license) stored as `pNN-*.jpg` in `images/`:

| Slot | File | Adobe Stock ID |
|------|------|----------------|
| Cover — plated meal | `p01-cover.jpg` | 259101953 |
| Doctor & patient | `p02-welcome.jpg` | 564639218 |
| Build-your-plate bowl | `p03-plate.jpg` | 1230460119 |
| Carb-smart foods | `p06-foods.jpg` | 314384961 |
| Walking outdoors | `p09-move.jpg` | 357613659 |

The back-cover **clinic art (`p10-clinic.jpg.svg`) is a custom illustration**
showing "Garcia Family Medicine" — kept intentionally, since the only free
stock "clinic" results were institutional hospitals. Swap in a real exterior
photo of the practice any time by dropping `p10-clinic.jpg` into `images/` and
changing that one `src` in `index.html` from `…jpg.svg` to `…jpg`.

To replace any photo, overwrite the `pNN-*.jpg` file (keep the same name and a
similar aspect ratio — frames use `object-fit: cover`).

## Important
This booklet is **general education, not individualized medical or nutrition
advice**. Contact details on the back cover are marked fill-in placeholders
(`[phone]` / `[website]`). Patients should check with Garcia Family Medicine
before starting — especially with diabetes/blood-pressure medications,
pregnancy, or kidney disease.
