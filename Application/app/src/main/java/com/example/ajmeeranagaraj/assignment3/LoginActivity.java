package com.example.ajmeeranagaraj.assignment3;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class LoginActivity extends AppCompatActivity implements View.OnClickListener{

    private Button b_signin;
    private EditText username;
    private EditText password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        b_signin = (Button)findViewById(R.id.signin);
        b_signin.setOnClickListener(this);
    }

    public void signin(){
        Intent i = new Intent(LoginActivity.this, NavigationActivity.class);
        startActivity(i);
    }

    @Override
    public void onBackPressed(){

    }

    @Override
    public void onClick(View v) {
        if(v==b_signin){
            signin();
        }
    }
}
