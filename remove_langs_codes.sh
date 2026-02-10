#!/bin/bash

EXTENSIONS=(
    ".ab" ".aa" ".af" ".ak" ".sq" ".am" ".ar" ".hy" ".as" ".ay"
    ".az" ".bn" ".ba" ".eu" ".be" ".bho" ".bs" ".br" ".bg" ".my"
    ".ca" ".ceb" ".zh-Hans" ".zh-Hant" ".co" ".hr" ".cs" ".da" ".dv"
    ".nl" ".dz" ".en-orig" ".en" ".eo" ".et" ".ee" ".fo" ".fj" ".fil"
    ".fi" ".fr" ".gaa" ".gl" ".lg" ".ka" ".de" ".el" ".gn" ".gu"
    ".ht" ".ha" ".haw" ".iw" ".hi" ".hmn" ".hu" ".is" ".ig" ".id"
    ".iu" ".ga" ".it" ".ja" ".jv" ".kl" ".kn" ".kk" ".kha" ".km"
    ".rw" ".ko" ".kri" ".ku" ".ky" ".lo" ".la" ".lv" ".ln" ".lt"
    ".lua" ".luo" ".lb" ".mk" ".mg" ".ms" ".ml" ".mt" ".gv" ".mi"
    ".mr" ".mn" ".mfe" ".ne" ".new" ".nso" ".no" ".ny" ".oc" ".or"
    ".om" ".os" ".pam" ".ps" ".fa" ".pl" ".pt" ".pt-PT" ".pa" ".qu"
    ".ro" ".rn" ".ru" ".sm" ".sg" ".sa" ".gd" ".sr" ".crs" ".sn"
    ".sd" ".si" ".sk" ".sl" ".so" ".st" ".es" ".su" ".sw" ".ss"
    ".sv" ".tg" ".ta" ".tt" ".te" ".th" ".bo" ".ti" ".to" ".ts"
    ".tn" ".tum" ".tr" ".tk" ".uk" ".ur" ".ug" ".uz" ".ve" ".vi"
    ".war" ".cy" ".fy" ".wo" ".xh" ".yi" ".yo" ".zu"
)

for file in *; do
    [ -f "$file" ] || continue
    
    original_file="$file"
    
    for ext in "${EXTENSIONS[@]}"; do
        ext_lower=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
        file_lower=$(echo "$file" | tr '[:upper:]' '[:lower:]')
        
        if [[ "$file_lower" == *"$ext_lower" ]]; then
            ext_len=${#ext}
            new_name="${file:0:-$ext_len}"
            
            if [ -e "$new_name" ]; then
                echo "Skip: '$file' -> '$new_name' (exists)"
                break
            fi
            
            mv -- "$file" "$new_name"
            echo "Renamed: '$file' -> '$new_name'"
            break
        fi
    done
done
