#!/bin/bash

# Train a model on your custom dataset
python main.py \
  --dataset mydataset \
  --data_root ./datasets/data/mydataset \
  --num_classes 6 \
  --model deeplabv3plus_mobilenet \
  --output_stride 16 \
  --batch_size 8 \
  --val_batch_size 4 \
  --crop_size 512 \
  --crop_val \
  --lr 0.01 \
  --total_itrs 20000 \
  --val_interval 200 \
  --gpu_id 0 \
  --loss_type cross_entropy \
  --save_val_results \
  --ckpt checkpoints/your_checkpoint.pth

