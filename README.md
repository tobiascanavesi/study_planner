# Study Plan Organizer

![Study Planner](/img/study_planner.png)

Welcome to the Study Plan Organizer! This application helps you create a personalized study plan based on your available time slots and study materials.
For test it out, you can use the file eco1half.md or frankenstein1-2.md that are in the repository.

This app was tested with markdown files, but in the future it will be possible to use other formats.

## Getting Started

To get started with the Study Plan Organizer, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your_username/study-plan-organizer.git 
   ```
   Create your .env file with the API keys for OpenAI, Serper and optionally for for LangSmith and Agentops if you want to track the performance of the model. This is the example of you the .env file should look like:
   ```bash
    OPENAI_API_KEY=your_openai_api_key
    SERPER_API_KEY=your_serper_api_key
    LANGSMITH_API_KEY=your_langsmith_api_key
    AGENTOPS_API_KEY=your_agentops_api_key
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:
    You don't need to install all the dependencies that are in requirements.txt, because this requirement contains the following library that
    is not necessary for run the app and is only use for transform PDFs to markdown files [marker](https://github.com/VikParuchuri/marker), so if you want to use directly markdown files and you don't need to transform files you can install only the following libraries:
    ```bash
    pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29
    ```
    If you want to install all the dependencies you can run the following command:
   ```bash 
    cd study_planner
    pip install -r requirements.txt
    ```

3. **Run the Application**: Run the Application: Run the Streamlit application using the following command:
    ```bash 
    streamlit run app.py
    ```

4. **Use the Application**: Open your web browser and go to http://localhost:8501 to access the Study Plan Organizer. Follow the on-screen instructions to upload your study material and generate a personalized study plan.

5. **Output**: The application will generate a personalized study plan based on your available time slots and study materials you can check the intermediate steps in the files time_estimation.md and personalized_study_plan.md and the final study plan in the file final_study_plan.md.

![Study Planner](/img/study_planner.gif)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

If you like you can follow me at [LinkedIn](https://www.linkedin.com/in/tcanavesi/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.