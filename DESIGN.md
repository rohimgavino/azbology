# 🌿 DESIGN.md — Azbology Design System
> **Aesthetic Archetype:** *Editorial Organic & Mindful Zen Craftsmanship*  
> **Target Audience:** B2B Wholesale Buyers, Cafe & Hotel Operators, Global Importers, & Mindful Coffee/Tea Enthusiasts.

---

## 1. Philosophy & Aesthetic Vision

Azbology merges the volcanic warmth of Indonesian single-origin coffee with the mindful serenity of **Pucuk Hening** artisan tea. The design language must evoke:
* **Tactile & Natural:** Warm paper-like surfaces instead of harsh digital whites.
* **Serene & Mindful:** Generous whitespace, calm transitions, and uncluttered layouts.
* **High Craftsmanship & Transparency:** Clear provenance details, roast curves, and artisanal steeping rituals.

---

## 2. Color Palette & Semantic Tokens

### Core Neutral (Surfaces & Text)
* `--color-surface-primary`: `#FBF8F2` (Warm Oatmeal Paper)
* `--color-surface-secondary`: `#F0EAE1` (Alabaster Sand)
* `--color-surface-card`: `#FFFFFF` (Pure Studio Background for Product Packshots)
* `--color-text-primary`: `#232724` (Charcoal Slate / Dark Roasted Earth)
* `--color-text-muted`: `#6B7280` (Muted Warm Gray)

### Botanical & Coffee Accents
* `--color-brand-green`: `#1E3A2F` (Deep Forest Green — Represents Pucuk Hening & Agroforestry)
* `--color-brand-green-light`: `#2D5545` (Moss Green Accent)
* `--color-brand-coffee`: `#8B4513` (Warm Coffee Terracotta)
* `--color-brand-coffee-dark`: `#5C2C0C` (Dark Espresso Roasting)
* `--color-accent-ochre`: `#D4A373` (Golden Ochre / Raw Cane Sugar / Honey Harvest)

---

## 3. Typography Hierarchy

| Role | Font Family | Weight | Letter Spacing | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Headings (Latin)** | `Cormorant Garamond` / `Fraunces` | 600, 700 | `-0.01em` (Tight & Elegant) | Hero titles, editorial story headings, product names |
| **Headings (Chinese)**| `Noto Serif SC` (思源宋体) | 600, 700 | `normal` | Mandarin titles with oriental tea heritage feel |
| **Body & UI Elements**| `Plus Jakarta Sans` / `Inter` | 400, 500, 600 | `+0.01em` | High readability for tasting notes, forms, and specs |
| **Technical & Badges**| `Plus Jakarta Sans` | 700 (Uppercase)| `+0.08em` (Wide tracking) | Origin tags, MASL elevation, process badges |

---

## 4. Spacing & Layout Principles

* **Whitespace Philosophy:** Minimum section padding `py-16` to `py-28` (64px - 112px). Avoid dense e-commerce clutter; let every product breathe like an art exhibit.
* **Container Max Width:** `max-w-7xl` (1280px) for general content, `max-w-4xl` for focused editorial narratives.
* **Borders & Dividers:** Subtle and organic (`border-[#F0EAE1]` or `rgba(0,0,0,0.06)`). No harsh black borders.
* **Border Radius:**
  * Cards & Containers: `rounded-2xl` (16px) or `rounded-3xl` (24px) for organic, soft corners.
  * Buttons & Badges: `rounded-full` (Pill shape) to convey approachability and smoothness.

---

## 5. UI Components & Interaction Guidelines

### Buttons (CTAs)
* **Primary Gold (High Conversion):** Background `--color-accent-ochre` with dark charcoal text. Hover: brightens slightly with smooth shadow transition.
* **Primary Green (Brand Heritage):** Background `--color-brand-green` with white text.
* **Outline / Editorial:** Thin 1px border with transparent background and blur backdrop.

### Product Packshot Cards
* **Aspect Ratio:** Generous height with soft neutral background (`#F9F7F4`).
* **Hover Interaction:** Subtle image scale `scale-105` with `duration-300` easing.
* **Metadata Hierarchy:** 
  1. Small uppercase origin tag (e.g., `TEMANGGUNG ORIGIN`).
  2. Serif product name.
  3. Processing tag pill (e.g., `Honey Process` or `Bud & Two Leaves`).
  4. Tasting notes list with botanical icons.

### Internationalization & Trilingual Rules
* Default language: **English (EN)** for international trade.
* Secondary: **Mandarin (ZH)** with Noto Serif SC font fallback.
* Tertiary: **Bahasa Indonesia (ID)** for domestic buyers and farmers' context.
