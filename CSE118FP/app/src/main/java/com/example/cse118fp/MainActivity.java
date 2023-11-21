package com.example.cse118fp;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

import com.example.cse118fp.databinding.ActivityMainBinding;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;



public class MainActivity extends Activity {

    private TextView mTextView;
    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        SensorManager sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        Sensor heartRateSensor = sensorManager.getDefaultSensor(Sensor.TYPE_HEART_RATE);
        SensorEventListener sensorEventListener = new SensorEventListener() {
            @Override
            public void onSensorChanged(SensorEvent event) {
                float bpm = event.values[0];
                mTextView.setText(String.format("Heart Rate: %.0f BPM", bpm));
            }
            @Override
            public void onAccuracyChanged(Sensor sensor, int accuracy) {
                // Handle accuracy changes if needed
            }
        };

        if (heartRateSensor != null) {
            // Heart rate sensor is available, keep listening for data
            sensorManager.registerListener(sensorEventListener, heartRateSensor, SensorManager.SENSOR_DELAY_NORMAL);
        }
    }
}