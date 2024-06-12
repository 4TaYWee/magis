<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <EditText
        android:id="@+id/kwotaDoPrzeliczenia"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:hint="@string/kwota"
        android:inputType="numberDecimal"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Spinner
        android:id="@+id/walutaWejsciowa"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:entries="@array/waluty"
        app:layout_constraintBottom_toTopOf="@id/walutaWyjsciowa"
        app:layout_constraintEnd

...
        app:layout_constraintBottom_toTopOf="@id/walutaWyjsciowa"
        app:layout_constraintEnd_toStartOf="@id/walutaWyjsciowa"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/kwotaDoPrzeliczenia" />

    <Spinner
        android:id="@+id/walutaWyjsciowa"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:entries="@array/waluty"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/walutaWejsciowa" />

    <TextView
        android:id="@+id/kwotaWyliczona"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="20sp"
        android:textStyle="bold"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/walutaWyjsciowa" />

</androidx.constraintlayout.widget.ConstraintLayout>
