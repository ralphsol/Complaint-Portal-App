package com.example.ajmeeranagaraj.assignment3;

import android.app.Fragment;
import android.os.Bundle;
import android.text.Spanned;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by Sai Esvar on 26-03-2016.
 */
public class MyComplaintsFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        View rootView = inflater.inflate(R.layout.fragment_my_complaints , container, false);

        Spanned[] dataArray = {};

        List<Spanned> compdataList = new ArrayList<Spanned>(
                Arrays.asList(dataArray));

        ArrayAdapter<Spanned> complaintsAdapter =
                new ArrayAdapter<Spanned>(
                        getActivity(),
                        R.layout.template_complaint,
                        R.id.comp_title,
                        compdataList);

        ListView listView = (ListView) rootView.findViewById(R.id.comp_listView);
        listView.setAdapter(complaintsAdapter);

        return rootView;
    }
}
