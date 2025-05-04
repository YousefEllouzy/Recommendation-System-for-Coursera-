# Coursera Smart Course Recommender

## Overview

This project is a machine learning-based recommendation system designed to suggest similar Coursera courses based on a selected course. It uses natural language processing techniques to analyze course content and provide personalized recommendations.

## Problem Statement

With thousands of courses available online, learners often struggle to find the right course that matches their interests or learning path. This project aims to simplify that process by recommending relevant courses automatically.

## Objective

To build a smart course recommender system that:
- Understands course similarities based on content
- Helps users discover useful alternatives
- Enhances the learning experience on platforms like Coursera

## How It Works

1. **Data Collection**: The dataset includes course titles and descriptions from Coursera.
2. **Text Processing**: Course content is vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) to capture the importance of words.
3. **Similarity Measurement**: Cosine similarity is used to find courses that are most similar in content.
4. **Recommendation**: Based on the selected course, the system suggests the top 6 similar courses.

## Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit** (for web interface)
- **Pickle** (for saving models and data)

## Use Cases

- Students discovering new learning paths
- Platforms enhancing user engagement
- Educational tools offering intelligent search alternatives

## Outcome

The recommender system provides fast and relevant course suggestions, improving user satisfaction and helping learners make informed decisions.

## Future Improvements

- Add course ratings and user preferences
- Include multilingual support
- Integrate with live Coursera API for real-time updates

## Author

Yousef Ellouzey  
Graduation Project – Faculty of Engineering  
AI Track

