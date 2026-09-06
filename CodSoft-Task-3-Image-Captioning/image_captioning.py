import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch


# ============================================================
# CODSOFT AI INTERNSHIP - TASK 3
# IMAGE CAPTIONING AI
# ============================================================

print("=" * 65)
print("        CODSOFT AI INTERNSHIP - TASK 3")
print("             IMAGE CAPTIONING AI")
print("=" * 65)

print("\nLoading AI model...")
print("Please wait...\n")


# ------------------------------------------------------------
# Load pretrained BLIP image captioning model
# ------------------------------------------------------------

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

print("AI model loaded successfully!")
print(f"Running on: {device}")


# ------------------------------------------------------------
# Generate Caption
# ------------------------------------------------------------

def generate_caption(image_path):

    try:
        image = Image.open(image_path).convert("RGB")

        inputs = processor(
            images=image,
            return_tensors="pt"
        )

        inputs = {
            key: value.to(device)
            for key, value in inputs.items()
        }

        output = model.generate(
            **inputs,
            max_new_tokens=50,
            num_beams=5
        )

        caption = processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return caption

    except Exception as error:
        return f"Error: {error}"


# ------------------------------------------------------------
# Select Image
# ------------------------------------------------------------

def select_image():

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png"),
            ("JPG Files", "*.jpg"),
            ("JPEG Files", "*.jpeg"),
            ("PNG Files", "*.png")
        ]
    )

    if not file_path:
        return

    try:

        # Open image
        image = Image.open(file_path).convert("RGB")

        # Resize image for display
        display_image = image.copy()
        display_image.thumbnail((600, 400))

        photo = ImageTk.PhotoImage(display_image)

        image_label.config(
            image=photo,
            text=""
        )

        image_label.image = photo

        # Show status
        status_label.config(
            text="Analyzing image..."
        )

        root.update()

        # Generate caption
        caption = generate_caption(file_path)

        # Display caption
        caption_text.config(
            text=caption
        )

        status_label.config(
            text="Image analyzed successfully!"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Unable to process image:\n\n{error}"
        )

        status_label.config(
            text="Something went wrong."
        )


# ------------------------------------------------------------
# Main GUI
# ------------------------------------------------------------

root = tk.Tk()

root.title("AI Image Captioning - CodSoft Task 3")

root.geometry("800x750")

root.configure(
    bg="#f4f6f8"
)


# ------------------------------------------------------------
# Title
# ------------------------------------------------------------

title_label = tk.Label(
    root,
    text="AI IMAGE CAPTIONING",
    font=("Arial", 26, "bold"),
    bg="#f4f6f8",
    fg="#1f2937"
)

title_label.pack(
    pady=(25, 5)
)


subtitle_label = tk.Label(
    root,
    text="Upload an image and let AI describe it",
    font=("Arial", 13),
    bg="#f4f6f8",
    fg="#6b7280"
)

subtitle_label.pack(
    pady=(0, 20)
)


# ------------------------------------------------------------
# Select Image Button
# ------------------------------------------------------------

select_button = tk.Button(
    root,
    text="SELECT IMAGE",
    command=select_image,
    font=("Arial", 13, "bold"),
    padx=30,
    pady=12,
    cursor="hand2"
)

select_button.pack(
    pady=10
)


# ------------------------------------------------------------
# Image Display Area
# ------------------------------------------------------------

image_frame = tk.Frame(
    root,
    width=620,
    height=420,
    bg="white",
    relief="solid",
    borderwidth=1
)

image_frame.pack(
    pady=20
)

image_frame.pack_propagate(False)


image_label = tk.Label(
    image_frame,
    text="Your selected image will appear here",
    font=("Arial", 12),
    bg="white",
    fg="#9ca3af"
)

image_label.pack(
    expand=True
)


# ------------------------------------------------------------
# Status
# ------------------------------------------------------------

status_label = tk.Label(
    root,
    text="Ready - Select an image",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#6b7280"
)

status_label.pack(
    pady=5
)


# ------------------------------------------------------------
# Caption Heading
# ------------------------------------------------------------

caption_heading = tk.Label(
    root,
    text="GENERATED IMAGE CAPTION",
    font=("Arial", 16, "bold"),
    bg="#f4f6f8",
    fg="#1f2937"
)

caption_heading.pack(
    pady=(15, 5)
)


# ------------------------------------------------------------
# Caption Output
# ------------------------------------------------------------

caption_text = tk.Label(
    root,
    text="Select an image to generate a caption.",
    font=("Arial", 14),
    bg="white",
    fg="#111827",
    wraplength=650,
    padx=20,
    pady=20,
    relief="solid",
    borderwidth=1
)

caption_text.pack(
    padx=50,
    fill="x"
)


# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------

footer_label = tk.Label(
    root,
    text="CodSoft AI Internship • Task 3 • Image Captioning",
    font=("Arial", 10),
    bg="#f4f6f8",
    fg="#9ca3af"
)

footer_label.pack(
    pady=20
)


# ------------------------------------------------------------
# Start Application
# ------------------------------------------------------------

root.mainloop()
exit()