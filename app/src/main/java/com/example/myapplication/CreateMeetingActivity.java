package com.example.myapplication;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class CreateMeetingActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_meeting);

        EditText etSlackId = findViewById(R.id.etSlackId);
        EditText etDuration = findViewById(R.id.etDuration);
        EditText etTiming = findViewById(R.id.etAvailability);
        Button btnSubmit = findViewById(R.id.btnSubmitMeeting);

        btnSubmit.setOnClickListener(v -> {
            String slackId = etSlackId.getText().toString();
            String duration = etDuration.getText().toString();
            String timing = etTiming.getText().toString();

            if (slackId.isEmpty() || duration.isEmpty()) {
                Toast.makeText(this, "Fill all fields", Toast.LENGTH_SHORT).show();
                return;
            }

            // Backend call will go here
            Toast.makeText(this, "Meeting request sent", Toast.LENGTH_LONG).show();
            finish();
        });
    }
}
