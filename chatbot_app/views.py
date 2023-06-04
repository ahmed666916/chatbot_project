import openai
from django.shortcuts import render
from django.http import JsonResponse

api_key = "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"

def chatbot(request):
    if request.method == 'POST':
        # Get user input
        user_input = request.POST['user_input']

        # Call the ChatGPT API to get a response
        response = openai.Completion.create(
            engine='davinci',
            prompt=f"Conversation with a user:\nUser: {user_input}\nAI:",
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the response text from the API result
        bot_response = response.choices[0].text.strip()

        # Return the response as JSON
        return JsonResponse({'bot_response': bot_response})

    # If the request is not a POST, render the chatbot template
    return render(request, 'chatbot.html')


