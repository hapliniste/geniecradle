# APRES REFLEXION

Après reflexion, GenieCradle sera sûrement pas un fork direct de Exllama et sera plutôt un système qui se base sur Guidance, comme ça je pourrai utiliser aussi les autres systèmes.
Un point important de GenieCradle sera d'offrir (surement en utilisant langChain) différenmts systèmes pour pouvoir mettre en place rapidement:
- agents
- Vérification (majority voting, reflexion, ToT)
- Amélioration (CoT, ToT, reflexion)

**et de pouvoir facilement y connecter tout type de données, offrir une API facilement adaptable pour pouvoir utiliser les données de n'importe où (BDD, fichiers statiques,...).**

# GenieCradle: Filling the Holes with Language Model Predictions

"GenieCradle" aims to create a robust system that enables local Language Model (LLM) instances to fill "holes" in a predefined text by generating suitable words or phrases. The project will use "bias manipulation" to guide the models to select words from a predefined list, providing enhanced control over the output.

## Project Overview

This project aims to create an efficient, user-friendly system that leverages the capabilities of ExLlama and LLMs to generate suitable words or phrases to fill "holes" within a text. The system will also use advanced techniques to guide the model to select from a predetermined list of words using bias manipulation. 

The purpose is to provide enhanced control over language models, allowing them to generate more specific and targeted responses. This should result in a more predictable and reliable output, making the AI system more usable and effective in practical applications.

## Project Structure

1. **LLM Interface**: This will be the layer that directly interacts with ExLlama and the underlying LLM. It will handle model initialization, settings configuration, and generation requests.

2. **Text Processor**: This module will process input text, identify the "holes" to be filled, and pass the modified text to the LLM for generation.

3. **Bias Manipulator**: This is where the magic happens. This component will manipulate the biases in the language model to guide the word selection process, based on a predefined list of options.

4. **Output Processor**: Once the LLM generates the output, this module will process the output text, ensuring the generated words or phrases correctly fill the "holes" in the original text.

5. **Main Application**: This is the main entry point of the system. It will interact with the user, accept input, and coordinate between the other modules to produce the final output.

## Things to Consider

1. **Bias Manipulation**: While manipulating biases can be a powerful way to guide the output of the model, it's essential to be cautious. Too much manipulation might result in unnatural or incoherent outputs. The Bias Manipulator should be thoroughly tested and fine-tuned to strike the right balance.

2. **Hole Identification**: Accurately identifying "holes" within the text can be a complex task. The Text Processor should be equipped to handle a variety of cases, including different hole markers or structures, nested holes, and more.

3. **Efficiency**: When dealing with large language models and complex operations like bias manipulation, efficiency can become a significant concern. Efficient code, judicious use of resources, and careful management of the generation process are crucial to ensure the system remains responsive and usable.

4. **Model Settings**: Different tasks may require different model settings for optimal results. The LLM Interface should allow for flexible and easy adjustment of these settings.

## Pitfalls to Avoid

1. **Overcomplication**: While it's important to create a system that can handle a variety of cases and complexities, beware of overcomplicating the design or code. Strive for simplicity and clarity wherever possible.

2. **Under-testing**: Thorough testing is crucial, especially when working with AI and complex operations like bias manipulation. Make sure to test extensively and in a variety of scenarios.

3. **Neglecting Documentation**: Good documentation is essential, both for your own reference and for anyone else who may use or contribute to the project. Document your code, your design decisions, and any issues or considerations that come up during development.

Now that you have a comprehensive overview of the project and its structure, you're ready to embark on this exciting journey. Happy coding!

