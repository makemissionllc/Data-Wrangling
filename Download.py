import kagglehub

# Download latest version
path = kagglehub.dataset_download("saurograndi/airplane-crashes-since-1908")

print("Path to dataset files:", path)