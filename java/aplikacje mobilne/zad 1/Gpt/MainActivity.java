import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText editTextAmount, editTextResult;
    private Spinner spinnerFromCurrency, spinnerToCurrency;
    private double[][] conversionRates = {
            {1.0, 0.85, 0.72},  // USD
            {1.18, 1.0, 0.85},  // EUR
            {1.39, 1.18, 1.0}   // GBP
            // Dodaj inne kursy według potrzeb
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editTextAmount = findViewById(R.id.editTextAmount);
        editTextResult = findViewById(R.id.editTextResult);
        spinnerFromCurrency = findViewById(R.id.spinnerFromCurrency);
        spinnerToCurrency = findViewById(R.id.spinnerToCurrency);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.currencies, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        spinnerFromCurrency.setAdapter(adapter);
        spinnerToCurrency.setAdapter(adapter);
    }

    public void convertCurrency(View view) {
        String fromCurrency = spinnerFromCurrency.getSelectedItem().toString();
        String toCurrency = spinnerToCurrency.getSelectedItem().toString();
        double amount = Double.parseDouble(editTextAmount.getText().toString());

        double fromRate = getConversionRate(fromCurrency);
        double toRate = getConversionRate(toCurrency);

        double result = (amount / fromRate) * toRate;
        editTextResult.setText(String.valueOf(result));
    }

    private double getConversionRate(String currency) {
        switch (currency) {
            case "USD":
                return conversionRates[0][spinnerToCurrency.getSelectedItemPosition()];
            case "EUR":
                return conversionRates[1][spinnerToCurrency.getSelectedItemPosition()];
            case "GBP":
                return conversionRates[2][spinnerToCurrency.getSelectedItemPosition()];
            // Dodaj inne waluty według potrzeb
            default:
                return 1.0; // Domyślnie 1:1
        }
    }
}
