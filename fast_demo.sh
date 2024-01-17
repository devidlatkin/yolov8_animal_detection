#!/bin/bash

# Download and unpack the model
file_directory=$(dirname "$0")
model_name="2024_01_17_animals_detection"
archive_name="$model_name.tar.gz"
models_storage_path="$file_directory/runs/detect"
inference_model_path="$models_storage_path/$model_name/weights/best.pt"
model_id="1Ie4y0eEgrpFHgfYld4Gl4nbp6zN0qn-Y"

if [ -f "$inference_model_path" ]; then
    echo "Model $inference_model_path already exists."
else
    if [ -d "$models_storage_path" ]; then
       eche "Path to save models already exist."
    else
       echo "Creating path to save models."
       mkdir -p "$models_storage_path"
    fi

    cd "$models_storage_path"
    if [ -f "$archive_name" ]; then
       echo "Model $archive_name already downloaded."
    else
        gdown --id "$model_id"
    fi

    tar -xzvf "$archive_name"
    cd ../..
fi


if [ -z "$1" ]; then
    # No argument provided, use default inference path
    inference_path="./datasets/inference_dataset"
else
    inference_path=$1
fi

#  Run the inference
python inference.py --image_src $inference_path