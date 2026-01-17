#!/bin/bash

echo "Cleaning up AWS resources..."

# Lab 2 Terraform
if [ -d "lab2/terraform" ]; then
    echo "Destroying Lab 2 infrastructure..."
    cd lab2/terraform
    terraform destroy -auto-approve
    cd ../..
fi

# Remove zip files
find . -name "*.zip" -type f -delete

echo "✅ Cleanup complete!"
echo "Note: Delete Bedrock Agents manually in AWS Console"
