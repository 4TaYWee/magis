package com.example.kalendarz;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.Calendar;
import java.util.List;

public class FragmentDay extends Fragment {

    private RecyclerView recyclerView;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_day, container, false);

        recyclerView = view.findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));

        // Pobranie argumentów przekazanych do fragmentu
        long timestamp = getArguments().getLong("timestamp");

        // Załadowanie wydarzeń na dany dzień
        List<Event> events = loadEventsForDay(timestamp);

        // Ustawienie adaptera recyclera
        EventAdapter adapter = new EventAdapter(events);
        recyclerView.setAdapter(adapter);

        return view;
    }
}
