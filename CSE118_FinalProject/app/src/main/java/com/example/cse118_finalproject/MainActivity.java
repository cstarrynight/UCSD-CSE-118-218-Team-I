package com.example.cse118_finalproject;

import static java.lang.Boolean.TRUE;

import android.Manifest;
import android.app.Activity;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.hardware.Sensor; //step 4 : import library
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager; //step 4 : import library
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import com.example.cse118_finalproject.databinding.ActivityMainBinding;

import java.util.ArrayList;
import java.util.List;
/*https://developer.samsung.com/sdp/blog/en/2022/05/25/check-which-sensor-you-can-use-in-galaxy-watch-running-wear-os-powered-by-samsung
*   - Display accessible sensors (heart rate sensor)
 */
public class MainActivity extends Activity implements SensorEventListener{

    private TextView tv_heartRate;

    private ActivityMainBinding binding;
    private static final String TAG = "____Main___";

    private SensorManager mSensorManager;
    private Sensor mHeartRate;

    private float bpm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMainBinding.inflate(getLayoutInflater()); // binder for framelayout
        setContentView(binding.getRoot());

        tv_heartRate = binding.textHEARTRATE;

        mSensorManager = ((SensorManager) getSystemService(SENSOR_SERVICE));
        mHeartRate = mSensorManager.getDefaultSensor(Sensor.TYPE_HEART_RATE);
        checkPermission();
        checkSensorAvailability();
    }

    private void checkPermission() { // step 3 started (according to content detail)

        // Runtime permission ------------
        if (checkSelfPermission(Manifest.permission.BODY_SENSORS) // check runtime permission for BODY_SENSORS
                != PackageManager.PERMISSION_GRANTED) {

            requestPermissions(
                    new String[]{Manifest.permission.BODY_SENSORS}, 1); // If BODY_SENSORS permission has not been taken before then ask for the permission with popup
        } else {
            Log.d(TAG, "ALREADY GRANTED"); //if BODY_SENSORS is allowed for this app then print this line in log.
        }
    }

    private void checkSensorAvailability() {
        //SensorManager mSensorManager = ((SensorManager) getSystemService(SENSOR_SERVICE)); //Step 5: SensorManager Instantiate

        //List of integrated sensor of device---------
        List<Sensor> sensors = mSensorManager.getSensorList(Sensor.TYPE_ALL); //Step 6: List of integrated sensors.
        ArrayList<String> arrayList = new ArrayList<String>();
        for (Sensor sensor : sensors) {

            arrayList.add(sensor.getName()); // put integrated sensor list in arraylist
        }
        Log.d(TAG, " " + arrayList); // print the arraylist in log.
        //check accessibility for 3rd party developers/public-------
        if ((mHeartRate) != null) { //Step 7: Check for particular sensor, if return value then the sensor is accessible
            tv_heartRate.setText(tv_heartRate.getText() + " Accessible"); // Show textView
            tv_heartRate.setTextColor(Color.parseColor("#32cd32")); //text color of textView
        } else { //Step 6: If return null, then sensor is not accessible and entered into else method.
            tv_heartRate.setText(tv_heartRate.getText() + " Inaccessible");
            tv_heartRate.setTextColor(Color.parseColor("#FF0000")); // textColor
        }
    }
    @Override
    protected void onResume() {
        super.onResume();
        mSensorManager.registerListener(this, mHeartRate, SensorManager.SENSOR_DELAY_NORMAL);
    }
    @Override
    protected void onPause() {
        super.onPause();
        mSensorManager.unregisterListener(this);
    }
    @Override
    public void onSensorChanged(SensorEvent event) {
        if(TRUE){//event.accuracy >= mSensorManager.SENSOR_STATUS_ACCURACY_MEDIUM
            //bpm = event.TYPE_HEART_RATE;
            bpm = event.values[0];
            tv_heartRate.setText(String.format("Heart Rate: %.0f BPM", bpm));
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
    }
}


