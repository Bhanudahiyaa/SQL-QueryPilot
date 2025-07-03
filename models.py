import google.generativeai as genai

genai.configure(api_key="AIzaSyA70viEjmSoRe2XWoAEjsiaI4EbZ003pI0")

models = genai.list_models()
for m in models:
    print(m.name, "->", m.supported_generation_methods)