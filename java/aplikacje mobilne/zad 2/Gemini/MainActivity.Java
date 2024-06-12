public class MainActivity extends AppCompatActivity {

    private EditText miastoEditText;
    private Button pobierzButton;
    private TextView aktualnaPogodaTextView;
    private TextView prognozaTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        miastoEditText = findViewById(R.id.miastoEditText);
        pobierzButton = findViewById(R.id.pobierzButton);
        aktualnaPogodaTextView = findViewById(R.id.aktualnaPogodaTextView);
        prognozaTextView = findViewById(R.id.prognozaTextView);

        pobierzButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String miasto = miastoEditText.getText().toString();
                pobierzPogode(miasto);
            }
        });
    }

    private void pobierzPogode(String miasto) {
        // Retrofit configuration
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("https://api.openweathermap.org/data/2.5/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        WeatherService service = retrofit.create(WeatherService.class);

        // API call with your API key
        Call<WeatherData> call = service.getWeatherData(miasto, "pl", "metric", YOUR_API_KEY);

        call.enqueue(new Callback<WeatherData>() {
            @Override
            public void onResponse(Call<WeatherData> call, Response<WeatherData> response) {
                if (response.isSuccessful()) {
                    WeatherData data = response.body();
                    // Parse and display data
                    aktualnaPogodaTextView.setText("Aktualna pogoda: " + data.getMain().getTemp() + "°C");
                    prognozaTextView.setText("Prognoza na jutro: " + data.getDaily().get(1).getTemp().getDay() + "°C");
                } else {
                    Toast.makeText(MainActivity.this, "Błąd pobierania danych pogodowych", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public  void onFailure(Call<WeatherData> call, Throwable t) {
                Toast.makeText(MainActivity.this, "Błąd sieci", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
