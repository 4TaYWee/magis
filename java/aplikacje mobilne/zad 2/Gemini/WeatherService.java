public interface WeatherService {

    @GET("weather")
    Call<WeatherData> getWeatherData(@Query("q") String city,
                                     @Query("lang") String language,
                                     @Query("units") String units,
                                     @Query("appid") String apiKey);
}
