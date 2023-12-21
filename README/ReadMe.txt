
	# TASK 1: Image Generation

(At this stage, I worked with Google Colab)
Python Code: 'adcreative_ai_task_1.py'

## Purpose:
- The aim of this task was to generate a new image that incorporates a given logo within a specific scene depiction.

## Method:
- Using the Stable Diffusion Img2Img model, a peaceful garden scene featuring a disposable coffee cup on a table under the morning
sun with a distinctive logo was created.

## Technologies:
+ JAX
+ NumPy
+ Flax
+ PIL (Python Imaging Library)
+ Diffusers library

## How It Works:
1. An RNG key is created.
2. The initial image is loaded and resized to pixel.
3. The model is prompted to generate a new image using a specific text prompt.
4. The generated image is displayed.

## Result:
- The result is an image of a coffee cup adorned with an original logo, including design details and colors.
- Image: Task-1__Output-Image.png



	# TASK 2: Dynamic Ad Template Creation

(At this stage, I worked with Google Colab)
Python Code: 'adcreative_ai_task_2.py'

## Purpose:
- Task 2 aimed to develop an ad template using the image generated in Task 1.

## Method:
- The Pillow library was used to edit the logo and image, and then custom text and a call-to-action button were added.

## Steps:
1. A white background is created.
2. The logo and the image from Task 1 are added to the background.
3. The Playfair Display SemiBold font is used to write the punchline and button text.
4. The final ad template is saved and displayed.

## Result:
- The result is a dynamic ad template featuring the company's logo, a customized punchline, and a button.
- Image: Task-2__Output-Image.png



	# TASK 3: API Development

(At this stage, I worked with Visual Studio Code)
Python Code: 'main.py'

## Purpose:
- Task 3 was to develop an API that allows users to create personalized ad visuals using uploaded images.

## Method:
- A fast and efficient API was developed using FastAPI.

## Steps:
1. An API application is created with FastAPI.
2. Endpoints and parameters are defined.
3. Image uploading, text placement, and button drawing processes are carried out.
4. The visual result is converted into a byte array and sent as an API response.

## API Features:
+ Endpoint: `/create-ad/`
+ Parameters: `image`, `logo`, `color_hex`, `punchline`, `button_text`
+ Response: The generated ad visual in PNG format as a byte array.

## Result:
- After running the 'main.py' file in the terminal, the desired tests can be performed with the URL that opens.
All the steps I carried out after the URL is opened are also demonstrated with photos named 'API_Photo-...'.



	# BONUS: Establishing a structure that can receive multiple requests simultaneously and work in parallel

- The 'main.py' file is designed accordingly. Running the application using multiple threads or processes increases the capacity
to process parallel requests. For example, a command like "uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000" starts the
application with four threads. This allows the application to process multiple requests at the same time.
