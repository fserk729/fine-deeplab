#!/bin/bash

# Train a model on your custom dataset
python ./DeepLabV3Plus-Pytorch/main.py \
  --dataset mydataset \
  --data_root /mnt/Data1/fserkeyn/fserkeyn_deeplab_fine_train/fine-deeplab/_data/mydataset \
  --num_classes 6 \
  --model deeplabv3plus_mobilenet \
  --output_stride 16 \
  --batch_size 16 \
  --val_batch_size 8 \
  --crop_size 640 \
  --crop_val \
  --lr 0.01 \
  --total_itrs 1000 \
  --val_interval 20 \
  --print_interval 5 \
  --gpu_id 0 \
  --loss_type cross_entropy \
  --ckpt checkpoints/your_checkpoint.pth \
  --enable_vis \
  --vis_env 'run2' \
  --vis_port 13570 \
  --save_val_results
