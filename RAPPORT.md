# Rapport d'optimisation des images

**185 images traitées** sans erreur.

## Bilan global

- Poids avant : **10.22 Mo**
- Poids après : **3.15 Mo**
- Gain : **69.2 %**
- Photos redimensionnées : 23 (les grosses photos téléphone qui faisaient 2000+ px)
- Photos juste ré-optimisées : 162 (déjà ≤ 600 px, taille préservée)

## Format appliqué

- **Long côté maximum : 600 px** (le ratio largeur/hauteur est strictement préservé)
- **JPEG qualité 85** + progressif + sous-échantillonnage 4:2:0
- **PNG optimisés**, transparence préservée pour les logos
- **Sharpening léger** appliqué après redimensionnement (compense la perte de netteté)
- **Rotation EXIF appliquée** (les photos téléphone s'affichent dans le bon sens)
- **Métadonnées EXIF supprimées** (GPS, modèle d'appareil, etc.)
- **Noms de fichiers strictement préservés**

## Top 15 des plus gros gains

| Fichier | Dimensions | Avant | Après | Économie |
|---------|------------|-------|-------|----------|
| germaine.jpg | 2176×3136 → 416×600 | 820 Ko | 48 Ko | −772 Ko |
| cuisine.jpg | 2245×3987 → 338×600 | 818 Ko | 51 Ko | −767 Ko |
| patrick.jpg | 2140×3468 → 370×600 | 715 Ko | 60 Ko | −655 Ko |
| no#U00ebl.jpg | 1699×2538 → 402×600 | 571 Ko | 45 Ko | −526 Ko |
| lo#U00efc_enfant.jpg | 1430×2144 → 400×600 | 561 Ko | 54 Ko | −506 Ko |
| olivier.jpg | 2208×2944 → 450×600 | 520 Ko | 38 Ko | −482 Ko |
| claudia.jpg | 1694×2048 → 496×600 | 502 Ko | 59 Ko | −443 Ko |
| Emile.jpg | 1536×2048 → 450×600 | 476 Ko | 81 Ko | −395 Ko |
| melwyn.jpg | 1520×2048 → 445×600 | 422 Ko | 38 Ko | −384 Ko |
| famille.jpg | 1600×900 → 600×338 | 428 Ko | 63 Ko | −365 Ko |
| famille_1.jpg | 1600×900 → 600×338 | 425 Ko | 62 Ko | −363 Ko |
| chien.jpg | 2000×1126 → 600×338 | 279 Ko | 48 Ko | −230 Ko |
| mathilde.jpg | 1536×2048 → 450×600 | 274 Ko | 52 Ko | −222 Ko |
| louane.jpg | 1638×2048 → 480×600 | 192 Ko | 22 Ko | −170 Ko |
| barbara.jpg | 1536×2048 → 450×600 | 200 Ko | 39 Ko | −160 Ko |

## Photos basse résolution à surveiller (44)

Ces photos ont un long côté < 250 px à l'origine. Je ne les ai **pas** agrandies (ça les aurait rendues floues), mais sur les écrans modernes elles peuvent paraître pixellisées si affichées en grand. Tu pourrais envisager de les remplacer par des versions plus grandes quand tu auras le temps :

- `machine_#U00e0_caf#U00e9.webp` (200×200)
- `alto.jpg` (225×225)
- `animaux.jpg` (225×225)
- `batterie.jpg` (225×225)
- `brosses_instruments.jpg` (224×225)
- `caf#U00e9_des_sapins.jpg` (225×225)
- `chevreuil.jpg` (225×225)
- `cornettes.jpg` (225×225)
- `coulisses.jpg` (225×224)
- `drapeau_contheysanne.jpg` (225×225)
- `escalier.jpg` (225×225)
- `four.jpg` (225×225)
- `grosse_caisse.jpg` (225×225)
- `habits.jpg` (225×225)
- `helvetia_ass.jpg` (225×225)
- `lasagnes.jpg` (225×225)
- `meuble_salon.jpg` (225×225)
- `migros.jpg` (225×225)
- `pneu.jpg` (225×225)
- `poire.jpg` (225×225)
- `pomme_terre.jpg` (225×225)
- `pull.jpg` (225×225)
- `saucisse.jpg` (225×225)
- `savon.jpg` (225×225)
- `table_jardin.jpg` (225×225)
- `tasse.jpg` (225×225)
- `un_pull.jpg` (225×225)
- `vin_rouge.jpg` (225×224)
- `arome_maggy.webp` (226×226)
- `mur.jpg` (228×221)
- ... et 14 autres

## Comment intégrer dans GitHub

1. Dézippe `images-optimized.zip` sur ton ordinateur.
2. Sur ton repo GitHub `olaf-programmeur/images`, supprime les anciennes images (ou plus simple : remplace-les en uploadant les nouvelles par-dessus).
3. Les noms de fichiers étant strictement identiques, **aucune modification n'est nécessaire dans `data.xlsx`** : les URLs `https://raw.githubusercontent.com/olaf-programmeur/images/main/...` continuent de fonctionner.
4. Astuce : tu peux glisser-déposer tous les fichiers d'un coup directement sur l'interface web de GitHub (bouton « Add file » → « Upload files »).