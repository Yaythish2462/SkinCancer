from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def read_predictions_from_file(file_path):
    predictions = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                class_id = 8  # Assuming class ID is always 8
                x_center, y_center, width, height = map(float, parts)
                predictions.append((class_id, x_center, y_center, width, height))
    return predictions

def write_predictions_to_file(predictions, file_path):
    with open(file_path, 'w') as file:
        for pred in predictions:
            file.write(' '.join(map(str, pred)) + '\n')

def ensemble_average(predictions1, predictions2):
    combined_predictions = []

    for pred1, pred2 in zip(predictions1, predictions2):
        combined_confidence = (pred1[1] + pred2[1]) / 2.0
        combined_box = (
            (pred1[2] + pred2[2]) / 2.0,
            (pred1[3] + pred2[3]) / 2.0,
            (pred1[4] + pred2[4]) / 2.0,
            (pred1[5] + pred2[5]) / 2.0,
        )

        combined_predictions.append((pred1[0], combined_confidence) + combined_box)

    return combined_predictions

def visualize_predictions(image_path, predictions, title="Predictions"):
    image = Image.open(image_path)

    fig, ax = plt.subplots(1)
    ax.imshow(image)

    for pred in predictions:
        class_id, confidence, x_center, y_center, width, height = pred
        x, y, w, h = (
            x_center - width / 2,
            y_center - height / 2,
            width,
            height,
        )

        rect = patches.Rectangle(
            (x, y),
            w,
            h,
            linewidth=1,
            edgecolor="r",
            facecolor="none",
            label=f"Class: {int(class_id)}, Confidence: {confidence:.2f}",
        )

        ax.add_patch(rect)

    plt.title(title)
    plt.show()

# Replace the following file paths with your actual file paths
image_path = r"C:\Users\YAYTHISH KANNAA G S\Downloads\420.jpeg"
file_path_model1 = r"C:\Users\YAYTHISH KANNAA G S\Downloads\yolov5420.txt"
file_path_model2 = r"C:\Users\YAYTHISH KANNAA G S\Downloads\420.txt"

# Read predictions from files
predictions_model1 = read_predictions_from_file(file_path_model1)
predictions_model2 = read_predictions_from_file(file_path_model2)

# Perform ensemble averaging
combined_predictions = ensemble_average(predictions_model1, predictions_model2)
print(combined_predictions)
# Write combined predictions to a new file
write_predictions_to_file(combined_predictions, 'combined_predictions.txt')

# Visualize combined predictions on the image
visualize_predictions(image_path, combined_predictions, title="Combined Predictions")
