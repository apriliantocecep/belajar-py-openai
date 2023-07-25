from flask import make_response, jsonify, request
import openai


class MainController:

    def ask(self):
        payload = request.get_json()
        if 'question' in payload:
            question = payload['question']
            res = openai.Completion.create(
                engine="text-davinci-002",
                prompt=question,
                max_tokens=100
            )

            answer = res['choices'][0]['text'].strip()

            return make_response(jsonify({"answer": answer}), 200)

        return make_response(jsonify({"error": "No question provided"}), 400)
