#!/bin/bash

# quickly run docker compose on all compose dirs
# this assumes the following path structure
# chall_type/chall_category/chall_name/some_folder/docker-compose.yml
# select chall_type by using

adjust_title() {
        echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '_'
}

find -L . -type f -name docker-compose.yml | while read -r dc_path; do
        compose_dir=$(dirname "$dc_path")
        chall_dir=$(realpath "$compose_dir/..")
        chall_name=$(adjust_title "$(echo "$chall_dir" | rev | cut -d '/' -f 1 | rev)")
        cat_name=$(adjust_title "$(echo "$chall_dir" | rev | cut -d '/' -f 2 | rev)")
        type_name=$(adjust_title "$(echo "$chall_dir" | rev | cut -d '/' -f 3 | rev)")
        project_name="${type_name}_${cat_name}_$chall_name"

        if [[ -n "$CHALL_TYPE" ]] && [[ "$type_name" != "$CHALL_TYPE" ]]; then
                echo "SKIPPING $project_name"
                continue
        fi

        pushd "$compose_dir" || exit
        docker compose -p "$project_name" "$@"
        popd || exit
done
