package com.example.kalendarz;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CalendarView;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Calendar;

public class MainActivity extends AppCompatActivity {

    private CalendarView calendarView;
    private EditText titleEditText;
    private EditText descriptionEditText;
    private Button addEventButton;
    private Button editEventButton;
    private Button deleteEventButton;
    private TextView eventDetailsTextView;

    private Event currentEvent; // Zmienna do przechowywania aktualnie wybranego wydarzenia

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        calendarView = findViewById(R.id.calendarView);
        titleEditText = findViewById(R.id.titleEditText);
        descriptionEditText = findViewById(R.id.descriptionEditText);
        addEventButton = findViewById(R.id.addEventButton);
        editEventButton = findViewById(R.id.editEventButton);
        deleteEventButton = findViewById(R.id.deleteEventButton);
        eventDetailsTextView = findViewById(R.id.eventDetailsTextView);

        // Ustawianie domyślnego wydarzenia na null
        currentEvent = null;

        // Dodawanie akcji do przycisków
        addEventButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                addEvent();
            }
        });

        editEventButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                editEvent();
            }
        });

        deleteEventButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                deleteEvent();
            }
        });

        // Obsługa kliknięcia daty w kalendarzu
        calendarView.setOnDateChangeListener(new CalendarView.OnDateChangeListener() {
            @Override
            public void onSelectedDateChanged(CalendarView view, int year, int month, int dayOfMonth) {
                loadEvent(year, month, dayOfMonth);
            }
        });
    }

    // Metoda do dodawania nowego wydarzenia
    private void addEvent() {
        String title = titleEditText.getText().toString();
        String description = descriptionEditText.getText().toString();

        // Pobranie wybranej daty z kalendarza
        Calendar calendar = Calendar.getInstance();
        calendar.set(calendarView.getYear(), calendarView.getMonth(), calendarView.getDayOfMonth());

        // Utworzenie nowego wydarzenia
        Event event = new Event(title, description, calendar.getTimeInMillis());

        // Zapisanie wydarzenia do pamięci (np. bazy danych)

        // Wyświetlenie informacji o wydarzeniu
        updateEventDetails(event);

        // Wyczyszczenie pól tekstowych
        titleEditText.setText("");
        descriptionEditText.setText("");
    }

    // Metoda do edycji istniejącego wydarzenia
    private void editEvent() {
        if (currentEvent != null) {
            String title = titleEditText.getText().toString();
            String description = descriptionEditText.getText().toString();

            // Zaktualizowanie istniejącego wydarzenia
            currentEvent.setTitle(title);
            currentEvent.setDescription(description);

            // Zapisanie zaktualizowanego wydarzenia do pamięci (np. bazy danych)

            // Wyświetlenie informacji o zaktualizowanym wydarzeniu
            updateEventDetails(currentEvent);
        }
    }

// ... (poprzedni kod)

    // Metoda do ładowania wydarzenia z pamięci (np. bazy danych)
    private void loadEvent(int year, int month, int dayOfMonth) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(year, month, dayOfMonth);

        // Pobranie wydarzenia z pamięci dla wybranej daty
        Event event = loadEventFromStorage(calendar.getTimeInMillis());

        // Ustawienie currentEvent na pobrane wydarzenie
        currentEvent = event;

        // Aktualizacja widoku szczegółów wydarzenia
        updateEventDetails(event);
    }

    // Metoda do aktualizacji widoku szczegółów wydarzenia
    private void updateEventDetails(Event event) {
        if (event != null) {
            String title = event.getTitle();
            String description = event.getDescription();

            eventDetailsTextView.setText("Tytuł: " + title + "\nOpis: " + description);

            // Włączanie przycisków edycji i usuwania
            editEventButton.setEnabled(true);
            deleteEventButton.setEnabled(true);
        } else {
            eventDetailsTextView.setText("Brak wydarzeń dla tej daty");

            // Wyłączanie przycisków edycji i usuwania
            editEventButton.setEnabled(false);
            deleteEventButton.setEnabled(false);
        }
    }

    // Metoda do ładowania wydarzenia z pamięci (np. bazy danych) - przykładowa implementacja
    private Event loadEventFromStorage(long timestamp) {
        // Tutaj należy zaimplementować logikę ładowania wydarzenia z pamięci
        // (np. z bazy danych) na podstawie znacznika czasu

        // Zwróć null, jeśli nie znaleziono wydarzenia
        return null;
    }
}

// Klasa definiująca wydarzenie
class Event {
    private String title;
    private String description;
    private long timestamp;

    public Event(String title, String description, long timestamp) {
        this.title = title;
        this.description = description;
        this.timestamp = timestamp;
    }

    // Gettery i settery dla pól title, description i timestamp
}

