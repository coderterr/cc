
from flask import Flask, request, jsonify

app = Flask(__name__)

EXCHANGE_RATE = 83

@app.route('/convert', methods=['GET'])
def convert_currency():
    amount_in_inr = request.args.get('amount', default=1, type=float)
    amount_in_usd = amount_in_inr * EXCHANGE_RATE
    return jsonify({
        'amount_in_inr': amount_in_inr,
        'amount_in_usd': amount_in_usd
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)


#CurrencyConverterClient.py
import java.net.URI;
import java.net.http.*;

public class CurrencyConverterClient {
    public static void main(String[] args) {
        
        HttpClient client = HttpClient.newHttpClient();
        String url = "http://localhost:5000/convert?amount=100";
        HttpRequest request = HttpRequest.newBuilder().uri(URI.create(url)).build();

        client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
              .thenApply(HttpResponse::body)
              .thenAccept(System.out::println)
              .join(); 
    }
}