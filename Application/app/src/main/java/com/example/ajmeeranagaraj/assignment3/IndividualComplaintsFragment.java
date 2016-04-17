package com.example.ajmeeranagaraj.assignment3;

import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

/**
 * Created by Sai Esvar on 26-03-2016.
 */
public class IndividualComplaintsFragment extends Fragment{
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        View rootView = inflater.inflate(R.layout.fragment_individual_complaints, container, false);
        return rootView;
    }
}
